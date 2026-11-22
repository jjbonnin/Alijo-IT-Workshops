# Worksheet 5: Production Outage Incident Post-Mortem Report
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## Incident Header
* **Incident ID:** `INC-401`
* **Responder Name(s):** 
* **Date:** 
* **Affected Host:** `alijo-srv01` (Ubuntu Server LTS)
* **Overall Incident Status:** `[ ] Resolved & Verified`  `[ ] Partially Resolved`

---

## 1. Fault Diagnosis & Remediation Log
Document each fault discovered during the Final Management Challenge, the exact diagnostic command that revealed it, its root cause, and the exact remediation command you applied:

### Fault 1: Apache2 Web Service / Configuration State
* **Diagnostic Command & Output:** 
* **Root Cause:** 
* **Remediation Command(s):** 
* **Verification Output:** 

### Fault 2: Web Root File Ownership & Permissions (`/var/www/html/status.html`)
* **Diagnostic Command & Output:** 
* **Root Cause:** 
* **Remediation Command(s):** 
* **Verification Output:** 

### Fault 3: Secrets Permissions Drift (`/srv/alijo-portal/.env`)
* **Diagnostic Command & Output:** 
* **Root Cause:** 
* **Remediation Command(s):** 
* **Verification Output:** 

### Fault 4: Host Firewall Rules (`ufw`)
* **Diagnostic Command & Output:** 
* **Root Cause:** 
* **Remediation Command(s):** 
* **Verification Output:** 

### Fault 5: Monitoring Script Execution (`server_report.sh`)
* **Diagnostic Command & Output:** 
* **Root Cause:** 
* **Remediation Command(s):** 
* **Verification Output:** 

---

## 2. Final Acceptance Checklist
Confirm all acceptance criteria are verified before submitting:

* `[ ]` `systemctl is-active apache2` returns `active` and `systemctl is-enabled apache2` returns `enabled`.
* `[ ]` `sudo apache2ctl configtest` returns `Syntax OK`.
* `[ ]` `curl -I http://<SERVER_IP>/status.html` from an external client returns `HTTP/1.1 200 OK`.
* `[ ]` `/srv/alijo-portal/.env` permissions are `640` (`rw-r-----`) owned by `root:webadmins`.
* `[ ]` `sudo ufw status numbered` shows `Status: active`, permits `22/tcp` and `80/tcp`, and blocks `23/tcp`.
* `[ ]` `./Scripts/server_report.sh` executes cleanly and outputs a complete health report.

---

## 3. Preventive Recommendations
List **two operational safeguards** your team would implement to prevent similar configuration drift and unauthorized changes after future maintenance windows:
1. 
2.
