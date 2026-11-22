# Challenge 1: Structured Incident Diagnosis with AI
**Workshop 2: AI IT Technician Assistant | Alijó IT Workshops**

---

## 1. Objective
In this challenge, you will act as an L2 IT Support Technician assisting an overworked L1 helpdesk. Instead of sending vague, incomplete questions to an AI assistant, you will structure raw ticket symptoms and Linux terminal logs into a high-context prompt, evaluate the AI's ranked hypotheses, and design safe verification steps before applying any changes.

---

## 2. Incident Ticket Scenario (`INC-2041`)
* **Reported By:** Accounting Department (`pc-acct-04`)
* **Priority:** High
* **User Complaint:** *"Since this morning's server maintenance, none of us can open the internal payroll portal at `http://payroll.alijo.local`. The browser just spins and says 'Unable to connect'. Ping to the server IP still works though!"*
* **Target Host:** `alijo-app01` (`Ubuntu 22.04.4 LTS`, IP: `192.168.20.15`)

### Raw Evidence Collected by L1 Technician
```text
$ ping -c 2 192.168.20.15
64 bytes from 192.168.20.15: icmp_seq=1 ttl=64 time=0.41 ms
64 bytes from 192.168.20.15: icmp_seq=2 ttl=64 time=0.38 ms

$ dig @192.168.20.10 payroll.alijo.local +short
192.168.20.15

$ systemctl is-active apache2
failed

$ journalctl -u apache2 -n 5 --no-pager
Nov 12 08:14:02 alijo-app01 systemd[1]: Starting The Apache HTTP Server...
Nov 12 08:14:02 alijo-app01 apachectl[1842]: AH00526: Syntax error on line 14 of /etc/apache2/sites-enabled/payroll.conf:
Nov 12 08:14:02 alijo-app01 apachectl[1842]: Invalid command 'ServerAliasName', perhaps misspelled or defined by a module not included in the server configuration
Nov 12 08:14:02 alijo-app01 systemd[1]: apache2.service: Main process exited, code=exited, status=1/FAILURE
Nov 12 08:14:02 alijo-app01 systemd[1]: Failed to start The Apache HTTP Server.
```

---

## 3. Step-by-Step Instructions

1. **Sanitize & Structure Your Prompt:**
   * Review the raw evidence above. Make sure no credentials or sensitive tokens are exposed.
   * Build a structured prompt that explicitly provides:
     * **System Context:** OS version and web server stack (`Ubuntu 22.04.4 LTS`, `Apache2`).
     * **What Already Works:** Layer 3 IP connectivity (`ping`) and DNS resolution (`dig` returning `192.168.20.15`) are confirmed healthy.
     * **Exact Error Output:** The `systemctl` and `journalctl` log lines.
     * **Constraints:** Ask for non-destructive read-only inspection commands first, exact config fix, syntax validation (`apache2ctl configtest`), and post-restart verification.

2. **Query Your AI Assistant & Audit the Output:**
   * Submit your prompt to the AI assistant.
   * Check whether the AI accurately identifies the invalid Apache directive (`ServerAliasName` instead of `ServerAlias`) on line 14 of `/etc/apache2/sites-enabled/payroll.conf`.
   * Verify that the AI includes `sudo apache2ctl configtest` **before** `sudo systemctl restart apache2`.

3. **Document Your Diagnosis:**
   * Record your prompt, the AI's root-cause analysis, and your verification checklist in the Workshop 2 incident worksheet.

---

## 4. Success Criteria
* Your prompt eliminates irrelevant guesswork by stating that ICMP and DNS are already verified.
* Your proposed remediation plan validates configuration syntax before restarting the daemon and confirms HTTP `200 OK` recovery with `curl -I http://payroll.alijo.local`.
