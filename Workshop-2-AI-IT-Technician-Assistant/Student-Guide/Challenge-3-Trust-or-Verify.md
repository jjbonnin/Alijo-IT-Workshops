# Challenge 3: Trust or Verify — Auditing Risky & Hallucinated AI Fixes
**Workshop 2: AI IT Technician Assistant | Alijó IT Workshops**

---

## 1. Objective
AI assistants frequently generate confident, plausible-looking commands that contain subtle syntax hallucinations, overly broad security permissions, or destructive side effects. In this challenge, you will audit **four AI-suggested troubleshooting responses**, identify every hidden flaw or risk, and write the safe, production-grade replacement command for each case.

---

## 2. Audit Cases ("Trust or Verify?")

### Case A — "Permission Denied" on a Web Application Directory
* **Junior Tech Question:** *"Apache cannot read `/var/www/intranet/index.html` after I uploaded it as `ubtadmin`. How do I fix permissions fast?"*
* **AI Suggested Fix:**
  ```bash
  sudo chmod -R 777 /var/www/intranet
  ```
* **Your Audit Tasks:**
  1. Why is `chmod -R 777` a critical security vulnerability on a production Linux server?
  2. Write the safe ownership (`chown`) and permission (`chmod`) commands granting read/execute access to `www-data` without making files world-writable.

---

### Case B — Blocked Web Traffic on Ubuntu Server
* **Junior Tech Question:** *"Users can ping `192.168.20.10`, and `apache2` is active, but `curl http://192.168.20.10` times out from another PC."*
* **AI Suggested Fix:**
  ```bash
  sudo ufw disable
  sudo iptables -F
  ```
* **Your Audit Tasks:**
  1. What happens to SSH brute-force protection and other listening internal ports if an administrator disables `ufw` completely?
  2. Write the targeted `ufw` command that permits inbound HTTP (`80/tcp`) while keeping the host firewall active.

---

### Case C — Cleaning Up Old Logs to Free Disk Space
* **Junior Tech Question:** *"`/var/log` is filling up disk space on our Ubuntu server. Give me a one-liner to clear old logs immediately."*
* **AI Suggested Fix:**
  ```bash
  sudo rm -rf /var/log/*
  ```
* **Your Audit Tasks:**
  1. What breaks when active log files and subdirectories under `/var/log` (such as `/var/log/apache2` or `/var/log/journal`) are deleted while daemons still hold open file descriptors?
  2. Provide the safe, built-in `systemd` command (`journalctl --vacuum-size=...` or `logrotate`) to reclaim journal disk space cleanly without breaking running services.

---

### Case D — Hallucinated Command & Flags
* **Junior Tech Question:** *"How do I check listening TCP ports and see which systemd service owns them on Ubuntu 22.04?"*
* **AI Suggested Fix:**
  ```bash
  sudo netstat --systemd-unit --listening-only -tcp
  ```
* **Your Audit Tasks:**
  1. Test or verify the flags above (`man ss` / `man netstat`). Which parts of this command are hallucinated?
  2. Write the modern, native `iproute2` command (`ss`) that accurately lists listening TCP/UDP sockets along with their owning process names and PIDs.

---

## 3. Deliverable & Verification Rules
1. Complete your audit notes and corrected commands in the Workshop 2 worksheet.
2. Verify every replacement command against official `man` pages (`man chmod`, `man ufw`, `man journalctl`, `man ss`) before submitting.
3. Never run the unedited "AI Suggested Fix" snippets from Cases A, B, or C on your lab VM.
