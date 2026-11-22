# Challenge 1 Reference Analysis: Log Analysis & Failing Service Diagnosis
**Workshop 2: AI as an IT Technician Assistant — Instructor Solution Guide**

---

## 1. Scenario Overview
* **Target Asset:** `Assets/sample-service.log` (or live `nginx.service` conflict on Ubuntu Desktop VM)
* **Student Role:** Junior IT Support Technician
* **Objective:** Collect local log evidence first, construct a structured 5-part technical prompt, evaluate the AI's diagnostic suggestions safely, and verify the true root cause on the Ubuntu VM without making blind configuration changes.

---

## 2. Raw Evidence Analysis (`Assets/sample-service.log`)
Key lines students should extract from the log before consulting any AI assistant:

* `nginx[2411]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)`
* `nginx[2411]: nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)`
* `systemd[1]: nginx.service: Control process exited, code=exited, status=1/FAILURE`

### Technical Breakdown
* **Confirmed Root Cause:** Another active process on the system is already listening on TCP port `80` (both IPv4 `0.0.0.0:80` and IPv6 `[::]:80`). When `systemd` attempts to start `nginx.service`, the kernel rejects the `bind()` system call with Linux error `98 (EADDRINUSE)`, causing the Nginx master process to exit immediately with status code `1`.

---

## 3. Model 5-Part Technical Prompt (Reference Example)
A high-scoring student prompt should resemble the following structure:

* **Role & Environment:** *"You are a Linux system administrator helping me troubleshoot an Ubuntu 24.04 Desktop VM."*
* **Goal:** *"Identify why nginx.service failed to start based on the log excerpt below and tell me how to diagnose which process is causing the conflict."*
* **Evidence:** *"Log lines: `nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)` and `nginx.service: Control process exited, code=exited, status=1/FAILURE`."*
* **Constraints:** *"Provide read-only diagnostic commands first. Do not suggest disabling the firewall or changing file permissions. Explain every flag used."*
* **Output Format:** *"List the 2 most likely causes, the exact verification command for each, and the safest resolution steps."*

---

## 4. Safe Verification & Resolution Steps
Students must audit the AI's proposed commands with `--help` or `man` before running them on the VM:

1. **Identify the Process Holding Port 80 (Read-Only):**
   * `sudo ss -tulpn | grep :80`
     * `-t`: show TCP sockets
     * `-u`: show UDP sockets
     * `-l`: show listening sockets only
     * `-p`: show process name and PID
     * `-n`: show numerical port numbers instead of service names
   * *Alternative:* `sudo lsof -i :80`
2. **Confirm Nginx Service & Configuration State:**
   * `systemctl status nginx --no-pager`
   * `sudo nginx -t` (validates Nginx configuration syntax without restarting the service)
3. **Safe Resolution (Depending on Lab Setup):**
   * **Option A (Conflicting Web Server, e.g., Apache2 or Python HTTP test server):**
     * Stop the conflicting service: `sudo systemctl stop apache2` (or terminate the test listener PID).
     * Start Nginx cleanly: `sudo systemctl start nginx`
     * Verify listening state: `sudo ss -tulpn | grep :80`
   * **Option B (Both Services Needed):**
     * Reconfigure Nginx's `listen` directive in `/etc/nginx/sites-available/default` to an unused port (such as `8080`), validate with `sudo nginx -t`, and reload with `sudo systemctl reload nginx`.

---

## 5. Common Student Mistakes to Watch For
* **Pasting vague summaries instead of raw logs:** Asking *"Why won't Nginx start on Ubuntu?"* without including `98: Address already in use`.
* **Blindly running `kill -9` on random PIDs:** Students should verify *which* service owns the PID via `ss -tulpn` or `ps -fp <PID>` before stopping it cleanly via `systemctl`.
* **Modifying `/var/www/html` permissions:** Some students misread a startup failure as a file permission error; remind them that `bind() ... Address already in use` is strictly a network socket conflict, not a filesystem permission issue.
