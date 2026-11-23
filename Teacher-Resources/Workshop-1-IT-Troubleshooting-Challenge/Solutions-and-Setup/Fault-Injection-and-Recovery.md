# Fault Injection & Recovery Guide
**Workshop 1: IT Troubleshooting Challenge | Alijó IT Workshops**

> **Confidentiality Notice:** This document is intended exclusively for instructors. Do not share with students. Use the following commands inside the Ubuntu VM to prepare each scenario and to recover the system if needed.

---

## Pre-Session Check

Before injecting network faults (Incidents 01, 02, or 06), confirm the exact NetworkManager connection profile name on the student VM (usually `"Wired connection 1"`):

    nmcli connection show

Ensure a clean snapshot named `BASELINE – BEFORE WORKSHOP` exists before modifying any settings.

---

### Incident 01 – Incorrect IP Configuration
* **Fault Injection:** Configure a static IPv4 address in the wrong subnet via NetworkManager (`nmcli`) or GUI Settings (e.g., `192.168.99.50/24` with gateway `192.168.99.1` when the lab network is `10.0.2.0/24` or `192.168.1.0/24`):

      sudo nmcli con mod "Wired connection 1" ipv4.method manual ipv4.addresses 192.168.99.50/24 ipv4.gateway 192.168.99.1
      sudo nmcli con up "Wired connection 1"

* **Expected Student Action:** Identify mismatch via `ip address` and `ip route`. Revert interface to DHCP or set the valid static IP provided by the instructor.
* **Recovery:** 

      sudo nmcli con mod "Wired connection 1" ipv4.method auto ipv4.addresses "" ipv4.gateway ""
      sudo nmcli con up "Wired connection 1"

---

### Incident 02 – DNS Resolution Failure
* **Fault Injection:** Set an invalid DNS server on the active connection and disable automatic DNS via DHCP:

      sudo nmcli con mod "Wired connection 1" ipv4.dns "192.0.2.1" ipv4.ignore-auto-dns yes
      sudo nmcli con up "Wired connection 1"

* **Expected Student Action:** Confirm `ping -c 4 1.1.1.1` works while `getent hosts example.com` fails. Check `resolvectl status` to spot the blackhole DNS (`192.0.2.1`).
* **Recovery:**

      sudo nmcli con mod "Wired connection 1" ipv4.dns "" ipv4.ignore-auto-dns no
      sudo nmcli con up "Wired connection 1"

---

### Incident 03 – Stopped System Service
* **Fault Injection:** Stop a non-critical service (e.g., `ssh`, `cups`, or `apache2` if installed):

      sudo systemctl stop ssh

* **Expected Student Action:** Check `systemctl status ssh` and `journalctl -u ssh -n 30`. Request permission to start the service.
* **Recovery:**

      sudo systemctl start ssh

---

### Incident 04 – Incorrect File Permissions
* **Fault Injection:** Create a target script/file in `/home/<user>/lab-files/report-generator.sh` and remove read/execute permissions:

      mkdir -p ~/lab-files
      printf '#!/bin/bash\necho "Report generated successfully."\n' > ~/lab-files/report-generator.sh
      chmod 000 ~/lab-files/report-generator.sh

* **Expected Student Action:** Inspect with `ls -l ~/lab-files/report-generator.sh`. Propose `chmod u+rx` or `chmod 750` (reject `chmod 777` if proposed and ask for least privilege).
* **Recovery:**

      chmod 750 ~/lab-files/report-generator.sh

---

### Incident 05 – Application Does Not Start
* **Fault Injection:** Ensure `/opt/lab-apps/app-monitor.py` exists and is executable (`chmod +x`), and ensure `/tmp/it-monitor/settings.conf` does **not** exist (`rm -rf /tmp/it-monitor`):

      sudo chmod +x /opt/lab-apps/app-monitor.py
      rm -rf /tmp/it-monitor

* **Expected Student Action:** Run `/opt/lab-apps/app-monitor.py`, read the `FATAL ERROR` output indicating `/tmp/it-monitor/settings.conf` is missing, create the directory and file, and re-run.
* **Recovery:**

      mkdir -p /tmp/it-monitor && touch /tmp/it-monitor/settings.conf

---

### Incident 06 – Surprise Incident (Connectivity Lost After a Change)
* **Fault Injection:** Remove the default gateway route temporarily (without breaking DHCP lease immediately):

      sudo ip route del default

* **Expected Student Action:** Notice ping to local LAN IPs works, but `ping 1.1.1.1` returns `Network is unreachable`. Check `ip route` and notice the `default via ...` line is missing compared to their baseline notes.
* **Recovery:** Restore the route using `sudo ip route add default via <GATEWAY_IP>` or restart the NetworkManager connection:

      sudo nmcli con up "Wired connection 1"
