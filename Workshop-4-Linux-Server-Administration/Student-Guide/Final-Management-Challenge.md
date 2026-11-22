# Final Management Challenge: Multi-Fault Production Outage Recovery
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Scenario Briefing
After an overnight maintenance window on the Alijó Web & Application Server (`alijo-srv01`), the on-call helpdesk reports multiple critical failures:
1. **External Web Outage:** Remote users attempting to reach `http://<SERVER_IP>/status.html` receive either a connection timeout or an `HTTP 403 Forbidden` error.
2. **Broken Web Service / Configuration Error:** The Apache2 web service fails to reload cleanly or is serving the wrong site configuration.
3. **Unauthorized Permissions Drift:** A junior contractor ran an overly permissive command on `/srv/alijo-portal/.env` (`666` world-writable) and locked out `www-data` from reading `/var/www/html/status.html` (`600` owned by `root:root`).
4. **Firewall Regression:** Inbound HTTP traffic (`80/tcp`) is blocked by `ufw`, while a legacy rule left an unused insecure port (`23/tcp` Telnet) allowed.
5. **Monitoring Script Broken:** `/usr/local/bin/server_report.sh` (or `Scripts/server_report.sh`) is missing execute (`+x`) permissions for administrators.

Your instructor will either run the automated fault-injection script on your VM or instruct you to apply the fault scenario from your baseline snapshot.

---

## 2. Mission Objectives & Acceptance Criteria
Restore `alijo-srv01` to a secure, fully operational production state without disabling `ufw` or using `chmod 777`. Specifically, you must verify all **six acceptance criteria**:

1. **Apache2 Service Healthy & Boot-Enabled:**
   * `systemctl is-active apache2` returns `active`.
   * `systemctl is-enabled apache2` returns `enabled`.
   * `sudo apache2ctl configtest` returns `Syntax OK`.
2. **Web Content Accessible (`HTTP 200 OK`):**
   * `curl -I http://<SERVER_IP>/status.html` from an external client (or host workstation) returns `HTTP/1.1 200 OK`.
   * `/var/www/html/status.html` is owned by `root:www-data` with permissions `644` (`rw-r--r--`).
3. **Secrets Hardened (`Least Privilege`):**
   * `/srv/alijo-portal/.env` is owned by `root:webadmins` with permissions `640` (`rw-r-----`) — zero world-read or world-write access.
4. **Firewall Hardened (`ufw` Active):**
   * `sudo ufw status verbose` shows `Status: active` with `Default: deny (incoming), allow (outgoing)`.
   * Only `22/tcp` (SSH) and `80/tcp` (HTTP) are permitted; port `23/tcp` is removed.
5. **Diagnostic Script Executable & Verified:**
   * `Scripts/server_report.sh` has `750` or `755` permissions and runs cleanly without errors.
6. **Complete Incident Post-Mortem Submitted:**
   * Every fault, diagnostic command, root cause, remediation command, and verification output is documented in **`Worksheets/Incident-Report.md`**.

---

## 3. Recommended Recovery Workflow
1. **Do Not Panic or Guess:** Follow the 5-layer troubleshooting model from `Logs-and-Troubleshooting.md`.
2. **Collect Evidence First:** Run `systemctl status apache2`, `sudo journalctl -u apache2 -n 20`, `sudo ufw status numbered`, and `ls -la /var/www/html /srv/alijo-portal` before changing anything.
3. **Remediate Incrementally:** Fix one layer at a time (service config -> file permissions -> firewall rules -> automation script) and verify after each step.
4. **Final End-to-End Test:** Run `./Scripts/server_report.sh` and test `curl -i http://<SERVER_IP>/status.html` from your host terminal.
