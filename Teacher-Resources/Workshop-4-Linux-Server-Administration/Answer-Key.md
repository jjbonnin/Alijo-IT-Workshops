# Instructor Answer Key & Verification Reference
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Worksheet 2 (`Users-Groups-and-Permissions-Record.md`) — Reference Answers

### Question 1: Why use `usermod -aG` instead of `usermod -G`?
* **Model Answer:** Running `usermod -G <group> <user>` without `-a` (append) overwrites the user's entire list of supplementary groups, accidentally stripping previously assigned privileges (such as `sudo` or `adm`). Adding `-aG` appends the new group while keeping existing supplementary memberships intact.

### Section 2: Expected Directory & File Permissions
* `/srv/alijo-portal`: `drwxr-x---` | Octal `750` | Owner `root` | Group `webadmins`
* `/srv/alijo-portal/index.html`: `-rw-r--r--` | Octal `644` | Owner `root` | Group `webadmins`
* `/srv/alijo-portal/.env`: `-rw-r-----` | Octal `640` | Owner `root` | Group `webadmins`

### Section 4: Reflection Question (`755` Directory vs. `640` `.env`)
* **Model Answer:** Yes, `audit_rui` could traverse `/srv/alijo-portal` (`x`) and list the filenames (`r`), seeing that `.env` exists. However, `audit_rui` still could **not** read the contents of `.env`, because `.env` has mode `640` (`rw-r-----`), granting zero read permissions to "others" (`o`) outside `root` and `webadmins`.

---

## 2. Worksheet 3 (`Service-Management-Record.md`) — Reference Answers

### Section 3: `systemctl reload` vs. `systemctl restart`
* **Model Answer:** `systemctl reload apache2` sends a signal to the running daemon to re-read its configuration files gracefully without terminating active worker processes or dropping established HTTP connections. `systemctl restart apache2` stops the service completely, kills all active connections, and starts a brand-new daemon process.

---

## 3. Worksheet 4 (`Bash-Script-Record.md`) — Reference Answers

### Section 4: `crontab` Entry for Daily 07:30 Execution
* **Model Crontab Line:**
  ```cron
  30 7 * * * /home/sysadmin/Alijo-IT-Workshops/Workshop-4-Linux-Server-Administration/Scripts/server_report.sh >> /var/log/server_health.log 2>&1
  ```

---

## 4. Worksheet 5 (`Incident-Report.md`) — Final Management Challenge Solutions

| Fault | Diagnostic Command | Root Cause | Exact Remediation Commands |
| :--- | :--- | :--- | :--- |
| **1. Apache2 Stopped** | `systemctl status apache2` | Service was stopped (`inactive (dead)`) after maintenance. | `sudo systemctl enable --now apache2` |
| **2. `/var/www/html/status.html` Locked (`403`)** | `ls -l /var/www/html/status.html` | Owned by `root:root` with mode `600`, blocking `www-data` from reading it. | `sudo chown root:www-data /var/www/html/status.html && sudo chmod 644 /var/www/html/status.html` |
| **3. `/srv/alijo-portal/.env` World-Writable (`666`)** | `ls -l /srv/alijo-portal/.env` | Overly permissive `666` permissions exposed sensitive credentials to any local user. | `sudo chown root:webadmins /srv/alijo-portal/.env && sudo chmod 640 /srv/alijo-portal/.env` |
| **4. `ufw` Blocking HTTP & Allowing Telnet** | `sudo ufw status numbered` | Port `80/tcp` was set to `DENY IN` and legacy insecure `23/tcp` was `ALLOW IN`. | `sudo ufw delete allow 23/tcp && sudo ufw delete deny 80/tcp && sudo ufw allow 80/tcp` |
| **5. `server_report.sh` Not Executable** | `ls -l Scripts/server_report.sh` | Missing execute (`+x`) permission bit (`644`). | `chmod 750 Workshop-4-Linux-Server-Administration/Scripts/server_report.sh` |
