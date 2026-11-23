# Troubleshooting Expected Outcomes & Verification Matrix (`INC-401`)
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Layer-by-Layer Expected Findings & Resolutions

| Fault # | Affected Layer | Symptom Observed | Diagnostic Command & Output | Exact Remediation | Post-Fix Verification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Service (`systemd`)** | Connection refused on port `80` | `systemctl is-active apache2` → `inactive` | `sudo systemctl enable --now apache2` | `systemctl is-active apache2` → `active` |
| **2** | **File Permissions (Web)** | `HTTP/1.1 403 Forbidden` on `/status.html` | `ls -l /var/www/html/status.html` → `-rw------- root root` | `sudo chown root:www-data /var/www/html/status.html && sudo chmod 644 /var/www/html/status.html` | `curl -i http://127.0.0.1/status.html` → `HTTP/1.1 200 OK` |
| **3** | **File Security (`.env`)** | Credentials readable/writable by all local users | `ls -l /srv/alijo-portal/.env` → `-rw-rw-rw- root root` | `sudo chown root:webadmins /srv/alijo-portal/.env && sudo chmod 640 /srv/alijo-portal/.env` | `stat -c "%a %U:%G" /srv/alijo-portal/.env` → `640 root:webadmins` |
| **4** | **Host Firewall (`ufw`)** | External HTTP traffic dropped; Telnet exposed | `sudo ufw status numbered` → `23/tcp ALLOW`, `80/tcp DENY` | `sudo ufw delete allow 23/tcp && sudo ufw delete deny 80/tcp && sudo ufw allow 80/tcp` | `sudo ufw status` → only `22/tcp` and `80/tcp` `ALLOW IN` |
| **5** | **Automation Script** | `Permission denied` running `server_report.sh` | `ls -l Scripts/server_report.sh` → `-rw-r--r--` (`644`) | `chmod 750 Workshop-4-Linux-Server-Administration/Scripts/server_report.sh` | `./Workshop-4-Linux-Server-Administration/Scripts/server_report.sh` exits `0` |

---

## 2. Final Instructor Sign-Off Checklist
* [ ] `curl -s http://<STUDENT_VM_IP>/status.html` returns `<h1>Alijo Status: Operational</h1>`.
* [ ] `sudo ufw status` shows `Status: active` with `23/tcp` completely removed.
* [ ] `stat -c "%a" /srv/alijo-portal/.env` returns `640`.
* [ ] `Worksheets/Incident-Report.md` contains pre-fix and post-fix command outputs for all 5 faults.
