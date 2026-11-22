# Expected Diagnoses & Solutions — Workshop 1
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

> **Confidentiality Notice:** This document is for the instructor only. It provides a quick reference to verify if students have correctly identified the root cause before they attempt a fix.

## Incident Cheat Sheet

| Incident | Primary Symptoms | Root Cause (The "Why") | Expected Diagnostic Command(s) | Expected Fix / Recovery |
| :--- | :--- | :--- | :--- | :--- |
| **01 – Incorrect IP Configuration** | Cannot access local network or internet. | The network interface is configured with a static IP in the wrong subnet (or wrong gateway). | `ip address`<br>`ip route` | Change IPv4 method to Automatic (DHCP) via GUI or `nmcli`, and restart the interface. |
| **02 – DNS Resolution Failure** | Pinging IP addresses works, but browsing websites or pinging domains fails. | A blackhole or invalid DNS server (e.g., `192.0.2.1`) was manually set, ignoring DHCP DNS. | `ping 1.1.1.1` (works)<br>`getent hosts google.com` (fails)<br>`resolvectl status` | Remove the manual DNS entry and re-enable automatic DNS via GUI or `nmcli`. |
| **03 – Stopped System Service** | A specific application or background service is not responding. | The system service (e.g., `ssh` or `apache2`) has been stopped and is inactive. | `systemctl status ssh`<br>`journalctl -u ssh -n 20` | `sudo systemctl start ssh` |
| **04 – Incorrect File Permissions** | "Permission denied" error when trying to run a specific script or read a file. | The target file has `000` (no access) or `-rw-r--r--` (no execute) permissions for the user. | `ls -l ~/lab-files/report-generator.sh` | `chmod 750 <file>` or `chmod u+rx <file>` (Reject `chmod 777` if proposed). |
| **05 – Application Does Not Start** | A custom application crashes immediately upon execution with a fatal error. | The application script requires a specific configuration directory and file (`/tmp/it-monitor/settings.conf`) that do not exist. | Running the script `./app-monitor.py` and reading the explicit output error carefully. | `mkdir -p /tmp/it-monitor`<br>`touch /tmp/it-monitor/settings.conf` |
| **06 – Surprise Incident (Gateway Lost)** | Local network works, but internet connectivity is suddenly lost. | The default route (gateway) was deleted from the routing table. | `ping 1.1.1.1` (Network Unreachable)<br>`ip route` (Notice missing `default via`) | `sudo ip route add default via <IP>` or restart the network interface. |

---

## How to use this document during the lab:

When a team's **Lead Technician** raises their hand to request approval to run a `sudo` command or apply a fix, ask them to show you their **Incident Log**. 
1. Check if their "Root Cause" matches the table above.
2. Check if their "Evidence" matches the expected diagnostic commands.
3. If they are guessing the symptom instead of the root cause (e.g., saying *"The internet is down"* instead of *"The DNS server is wrong"*), deny the change and ask them to run more diagnostic commands.
