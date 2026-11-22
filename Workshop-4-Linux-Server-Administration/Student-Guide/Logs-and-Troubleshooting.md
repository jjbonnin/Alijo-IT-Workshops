# System Logs and Structured Server Troubleshooting
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Objective
In this module, you will learn where Linux stores system, authentication, and application logs, how to query `systemd` journals efficiently with `journalctl`, and how to follow a structured 5-layer troubleshooting methodology when diagnosing broken services on Ubuntu Server.

---

## 2. Primary Log Locations on Ubuntu Server

| Log Path / Tool | What It Records | Common Diagnostic Command |
| :--- | :--- | :--- |
| `/var/log/syslog` | General system messages, cron jobs, and daemon events | `sudo tail -n 50 /var/log/syslog` |
| `/var/log/auth.log` | SSH login attempts, `sudo` privilege escalations, PAM events | `sudo grep "Failed password" /var/log/auth.log` |
| `/var/log/apache2/error.log` | Apache2 startup errors, syntax issues, permission denials | `sudo tail -n 30 /var/log/apache2/error.log` |
| `/var/log/apache2/access.log` | Incoming HTTP requests, client IPs, HTTP status codes (`200`, `403`, `404`) | `sudo tail -n 30 /var/log/apache2/access.log` |
| `journalctl` | Unified binary `systemd` journal for all services and kernel boot logs | `sudo journalctl -u apache2 -xe --no-pager` |

---

## 3. Five-Layer Linux Service Troubleshooting Methodology
Whenever a server application is unreachable or failing, work systematically from bottom to top rather than guessing:

1. **Layer 1 — Host Resources & Storage (`df -h`, `free -h`, `uptime`):**
   * Check whether a full root filesystem (`100% Use%`) or out-of-memory (`OOM`) event is preventing services from writing PID/lock files or logs.
2. **Layer 2 — Service & Process State (`systemctl status <service>`, `journalctl -u <service>`):**
   * Confirm the daemon is `active (running)`. If `failed`, read the exact exit code and configuration syntax error in `journalctl`.
3. **Layer 3 — Socket Binding (`ss -tulpn`):**
   * Verify the process is bound to the expected IP (`0.0.0.0` or `::` vs. `127.0.0.1` loopback only) and port (`22`, `80`, `443`).
4. **Layer 4 — Host Firewall & Routing (`ufw status verbose`, `ip -br -4 addr`, `ip route`):**
   * Confirm the interface is `UP`, the IP/subnet is accurate, and `ufw` permits inbound traffic on the target port.
5. **Layer 5 — File Ownership & Permissions (`ls -la`, `namei -l /path/to/file`):**
   * If a web server returns `HTTP 403 Forbidden`, verify that `www-data` has execute (`x`) traversal permission on every parent directory and read (`r`) permission on the target file.

---

## 4. Guided Diagnostic Drill (Practice Before the Final Challenge)
Run the following read-only investigation commands on your lab server to practice reading log evidence:

```bash
# 1. Inspect recent SSH and sudo authentication activity
sudo grep -E "Accepted|Failed|sudo:" /var/log/auth.log | tail -n 15

# 2. Check for any failed systemd units across the entire system
systemctl --failed

# 3. Inspect Apache2 error and access logs side by side
sudo tail -n 10 /var/log/apache2/error.log
sudo tail -n 10 /var/log/apache2/access.log

# 4. Trace full directory path permissions for the web root
namei -l /var/www/html/index.html
```

---

## 5. Preparation for the Final Challenge
Once you are comfortable tracing issues across logs, sockets, `ufw`, and POSIX permissions, proceed to **`Student-Guide/Final-Management-Challenge.md`** and document your root-cause investigation in **`Worksheets/Incident-Report.md`**.
