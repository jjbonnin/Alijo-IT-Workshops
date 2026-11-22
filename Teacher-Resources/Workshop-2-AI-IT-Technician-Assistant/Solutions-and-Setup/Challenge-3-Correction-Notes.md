# Challenge 3 Reference Analysis & Correction Notes
**Workshop 2: AI as an IT Technician Assistant — Instructor Solution Guide**

---

## 1. Scenario Overview
* **Target Scenario:** Scenario 03 — AI Audit & Critical Thinking Challenge (*Spot the Trap!*)
* **Student Role:** Senior Verification Auditor
* **Objective:** Identify the severe security and operational risks behind three dangerous AI-generated commands, verify safer alternatives using `man` pages and `--help`, and propose production-grade replacements without executing any destructive commands on the Ubuntu VM.

---

## 2. Detailed Risk Breakdown & Verified Safe Alternatives

### Trap 1: `sudo chmod -R 777 /var/www/html`
* **Security & Operational Risks:**
  * Grants read, write, and execute (`rwx`) permissions to **every local user and compromised process** on the system (`world-writable`).
  * Any low-privilege service or attacker who gains shell access can modify web files, inject malicious scripts, or plant web shells.
  * Sets the execute bit (`+x`) on static files (`.html`, `.css`, `.jpg`), which is unnecessary and violates the principle of least privilege.
* **Safe Production-Grade Alternative:**
  * Assign proper ownership to the web server user/group (`www-data`) and apply `755` (`rwxr-xr-x`) to directories and `644` (`rw-r--r--`) to files:
    * `sudo chown -R www-data:www-data /var/www/html`
    * `sudo find /var/www/html -type d -exec chmod 755 {} +`
    * `sudo find /var/www/html -type f -exec chmod 644 {} +`

---

### Trap 2: `sudo ufw disable`
* **Security & Operational Risks:**
  * Completely shuts down the host firewall (`Uncomplicated Firewall`), exposing **all** listening network ports (SSH, databases, internal admin panels, development services) to the entire network instead of opening only the required web traffic.
* **Safe Production-Grade Alternative:**
  * Keep UFW enabled and explicitly allow only the required HTTP/HTTPS ports (preserving existing SSH access rules):
    * `sudo ufw allow 'Nginx Full'` *(or `sudo ufw allow 80/tcp && sudo ufw allow 443/tcp`)*
    * `sudo ufw status verbose`

---

### Trap 3: `sudo rm -rf /var/log/*`
* **Security & Operational Risks:**
  * Destroys forensic and operational audit trails required to investigate security incidents or troubleshoot system failures.
  * Deletes subdirectories inside `/var/log/` (such as `/var/log/nginx/` or `/var/log/apache2/`), which causes services to fail on restart because their log directories no longer exist.
  * Unlinks open log files still held by running daemons (`rsyslogd`, `systemd-journald`), meaning disk space is often **not** freed until those services restart.
* **Safe Production-Grade Alternative:**
  * Use `journalctl --vacuum-size` (or `--vacuum-time`) for systemd journals and `logrotate` for managed text log rotation:
    * `sudo journalctl --vacuum-size=100M`
    * `sudo logrotate -f /etc/logrotate.conf`

---

## 3. Related Instructor Solutions in This Folder
* **Scenario 01 Solution:** `Challenge-1-Reference-Analysis.md`
* **Scenario 02 Solution:** `Challenge-2-Script-Solution.py`
