# Teacher Guide — Workshop 1: IT Troubleshooting Challenge
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

> **Confidentiality Notice:** This document is intended exclusively for instructors. Do not share this folder with students prior to or during the workshop.

---

## 1. Instructor Preparation Checklist

Before the students arrive, ensure the following setup is complete on all lab workstations:

* **Host Machine:** Windows PC verified with Oracle VM VirtualBox installed and updated.
* **Virtual Machine:** Ubuntu Desktop VM configured, updated, and tested for network access (Bridged or NAT depending on lab setup).
* **Baseline Snapshot:** A clean snapshot named `BASELINE – BEFORE WORKSHOP` must be created *before* injecting any faults.
* **Lab Assets:** Copy `app-monitor.py` (from `01-Problem-Solving/.../Assets/`) to `/opt/lab-apps/app-monitor.py` on the VM and grant execution permissions (`chmod +x /opt/lab-apps/app-monitor.py`) before taking the baseline snapshot.
* **Printed / Digital Materials:** Ensure teams have access to the `Student-Workbook.md`, `Incident-Cards.md`, `Diagnostic-Checklist.md`, and blank `Incident-Log.md` templates.

---

## 2. Classroom Management & Safety Rules

* **Strict VM Isolation:** Remind students repeatedly that all commands and changes must happen *inside* the Ubuntu VM. Host machine settings and school network configurations are strictly off-limits.
* **Approval Gate for `sudo`:** Students are instructed to ask for teacher approval before executing commands with `sudo` or modifying system-level configurations. Use this moment to ask: *"What is your hypothesis, and what do you expect this command to change?"*
* **Role Rotation:** Enforce the rotation of the **Lead Technician** role after every incident so all team members gain hands-on CLI experience.

---

## 3. Session Pacing & Facilitation Guide (180 Minutes)

| Time | Phase | Instructor Actions |
| :--- | :--- | :--- |
| **00:00 – 00:15** | **Briefing & Roles** | Introduce the scenario, divide into teams of 4–5, assign initial roles, and emphasize safety rules. |
| **00:15 – 00:35** | **Methodology** | Walk through the 7-step methodology. Stress the difference between a *symptom* and a *root cause*. |
| **00:35 – 00:55** | **Baseline Inspection** | Have students run baseline diagnostic commands (`ip a`, `ip r`, `resolvectl status`, `df -h`) and record normal values. |
| **00:55 – 01:55** | **Incident Rounds (1–5)** | Assign Incident Cards 01 through 05 (either sequentially via snapshots or across different VMs). Circulate to check `Incident-Log.md` entries before approving fixes. |
| **01:55 – 02:20** | **Surprise Incident (06)** | Restore VMs to baseline, inject Incident 06 silently (or swap machines), and hand out the Incident 06 brief. Observe how teams react under time pressure. |
| **02:20 – 02:40** | **Documentation** | Ensure teams finalize their `Final-Report-Template.md` with copied terminal outputs/screenshots. |
| **02:40 – 03:00** | **Presentations & Wrap-up** | Each team presents 1–2 incidents (focusing on evidence and verification). Grade using the `Assessment-Rubric.md`. |

---

## 4. Fault Injection & Recovery Guide (Incidents 01–06)

Use the following commands inside the Ubuntu VM to prepare each scenario.

### Incident 01 – Incorrect IP Configuration
* **Fault Injection:** Configure a static IPv4 address in the wrong subnet via NetworkManager (`nmcli`) or GUI Settings (e.g., set IP to `192.168.99.50/24` with gateway `192.168.99.1` when the lab network is `10.0.2.0/24` or `192.168.1.0/24`).
* **Expected Student Action:** Identify mismatch via `ip address` and `ip route`. Revert interface to DHCP or set the valid static IP provided by the instructor.
* **Recovery:** 
  ```bash
  sudo nmcli con mod "Wired connection 1" ipv4.method auto
  sudo nmcli con up "Wired connection 1"
  ```

### Incident 02 – DNS Resolution Failure
* **Fault Injection:** Set an invalid DNS server on the active connection and disable automatic DNS via DHCP:
  ```bash
  sudo nmcli con mod "Wired connection 1" ipv4.dns "192.0.2.1" ipv4.ignore-auto-dns yes
  sudo nmcli con up "Wired connection 1"
  ```
* **Expected Student Action:** Confirm `ping -c 4 1.1.1.1` works while `getent hosts example.com` fails. Check `resolvectl status` to spot the blackhole DNS (`192.0.2.1`).
* **Recovery:**
  ```bash
  sudo nmcli con mod "Wired connection 1" ipv4.dns "" ipv4.ignore-auto-dns no
  sudo nmcli con up "Wired connection 1"
  ```

### Incident 03 – Stopped System Service
* **Fault Injection:** Stop a non-critical service (e.g., `ssh`, `cups`, or `apache2` if installed):
  ```bash
  sudo systemctl stop ssh
  ```
* **Expected Student Action:** Check `systemctl status ssh` and `journalctl -u ssh -n 30`. Request permission to start the service.
* **Recovery:** 
  ```bash
  sudo systemctl start ssh
  ```

### Incident 04 – Incorrect File Permissions
* **Fault Injection:** Create a target script/file in `/home/<user>/lab-files/report-generator.sh` and remove read/execute permissions:
  ```bash
  mkdir -p ~/lab-files
  echo '#!/bin/bash\necho "Report generated successfully."' > ~/lab-files/report-generator.sh
  chmod 000 ~/lab-files/report-generator.sh
  ```
* **Expected Student Action:** Inspect with `ls -l ~/lab-files/report-generator.sh`. Propose `chmod u+rx` or `chmod 750` (reject `chmod 777` if proposed and ask for least privilege).
* **Recovery:** 
  ```bash
  chmod 750 ~/lab-files/report-generator.sh
  ```

### Incident 05 – Application Does Not Start
* **Fault Injection:** Ensure `/opt/lab-apps/app-monitor.py` exists and is executable (`chmod +x`), and ensure `/tmp/it-monitor/settings.conf` does **not** exist (`rm -rf /tmp/it-monitor`).
* **Expected Student Action:** Run `/opt/lab-apps/app-monitor.py`, read the `FATAL ERROR` output indicating `/tmp/it-monitor/settings.conf` is missing, create the directory and file, and re-run.
* **Recovery:** 
  ```bash
  mkdir -p /tmp/it-monitor && touch /tmp/it-monitor/settings.conf
  ```

### Incident 06 – Surprise Incident (Connectivity Lost After a Change)
* **Fault Injection:** Remove the default gateway route temporarily (without breaking DHCP lease immediately) or bring the link down/delete default route:
  ```bash
  sudo ip route del default
  ```
* **Expected Student Action:** Notice `ping` to local LAN IPs works, but `ping 1.1.1.1` returns `Network is unreachable`. Check `ip route` and notice the `default via ...` line is missing compared to their baseline notes.
* **Recovery:** Restore the route using `sudo ip route add default via <GATEWAY_IP>` or restart the NetworkManager connection:
  ```bash
  sudo nmcli con up "Wired connection 1"
  ```
