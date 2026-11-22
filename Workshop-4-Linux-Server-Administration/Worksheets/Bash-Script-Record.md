# Worksheet 4: Bash Server Monitoring Script Record
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## Student Details
* **Student Name(s):** 
* **Date:** 

---

## 1. Script Permissions & Execution Verification (`Scripts/server_report.sh`)
Before running `Scripts/server_report.sh`, inspect its permissions and make it executable (`chmod +x Scripts/server_report.sh` or `chmod 750 Scripts/server_report.sh`).

| Verification Item | Recorded Value / Command |
| :--- | :--- |
| **Script File Path** | `Workshop-4-Linux-Server-Administration/Scripts/server_report.sh` |
| **Permissions (`ls -l Scripts/server_report.sh`)** | |
| **Shebang Line (`head -n 1`)** | |
| **Exit Code After Execution (`echo $?`)** | |

---

## 2. Summary of Captured Health Report Metrics
Run `./Scripts/server_report.sh` and record key output values from each section:

* **Hostname & Kernel:** 
* **CPU Load Averages (`uptime`):** 
* **Root Filesystem Usage (`df -h /`):** 
* **Core Services (`ssh`, `apache2`, `ufw`):** 
* **Recent Authentication Failures Count:** 

---

## 3. Script Enhancement Task
Modify your local copy of `Scripts/server_report.sh` to add **one new health check** (for example: top 5 memory-consuming processes using `ps aux --sort=-%mem | head -n 6`, or available package updates, or `/var/log` disk usage with `du -sh /var/log`).

Paste the Bash snippet you added below:

```bash
# Paste your custom Bash health-check block here

```

---

## 4. Automation Reflection Question
How would you schedule `server_report.sh` to run automatically every morning at `07:30` and save its output to `/var/log/server_health.log` using `cron`? Write the exact `crontab` line below.
* **Crontab Entry:**
