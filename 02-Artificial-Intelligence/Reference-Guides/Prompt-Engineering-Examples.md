# Prompt Engineering Examples for IT Technicians
**02-Artificial-Intelligence | Alijó IT Workshops**

---

## 1. The 5-Part Technical Prompt Formula
Every high-quality IT troubleshooting prompt should combine five clear components:
1. **Role & Environment:** Exact OS, service stack, and lab/production context.
2. **Goal:** Specific diagnostic or debugging objective.
3. **Raw Evidence:** Sanitized terminal output, exact log lines, or source code.
4. **Constraints:** Safety rules (read-only checks first, least privilege, no firewall disabling).
5. **Output Format:** How you want the response structured (ranked causes, table, annotated script).

---

## 2. Weak vs. Effective Prompts (Side-by-Side)

### Example A: Failing Systemd Service Diagnosis

* **Weak Prompt (Avoid):**
  > "Nginx won't start on my Ubuntu server. How do I fix it?"
  *(Why it fails: Provides zero log evidence, forcing the AI to guess among dozens of unrelated causes and often suggesting risky permission or firewall changes.)*

* **Effective Prompt (Recommended):**
  > **Role & Environment:** You are a Linux system administrator helping troubleshoot an Ubuntu 24.04 LTS VM.  
  > **Goal:** Identify why `nginx.service` fails to start and provide read-only commands to confirm the conflicting process.  
  > **Evidence:**  
  > `nginx[2411]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)`  
  > `systemd[1]: nginx.service: Control process exited, code=exited, status=1/FAILURE`  
  > **Constraints:** Give read-only diagnostic commands first. Explain every flag. Never suggest `chmod 777` or disabling UFW.  
  > **Output Format:** 1) Confirmed root cause, 2) Exact verification command with flag breakdown, 3) Safe resolution options.

---

### Example B: Python / Bash Script Debugging

* **Weak Prompt (Avoid):**
  > "Fix this Python script for me: [pastes code without stating expected behavior or OS]"
  *(Why it fails: The AI may silently rewrite logic or introduce OS-incompatible commands without explaining what was broken.)*

* **Effective Prompt (Recommended):**
  > **Role & Environment:** You are a Python and Linux automation engineer reviewing a diagnostic script for Ubuntu 24.04.  
  > **Goal:** Find all syntax, logic, and security bugs in the script below before I test it in a sandbox VM.  
  > **Evidence:** `[Paste sanitized script code]`  
  > **Constraints:** Do not rewrite the script until you list each bug individually (line/function, bug type, impact). Replace unsafe shell calls with `subprocess.run` without `shell=True`.  
  > **Output Format:** A numbered bug report table followed by the corrected script with inline comments.

---

### Example C: Network & Firewall Troubleshooting

* **Weak Prompt (Avoid):**
  > "I can't reach my website on Ubuntu, should I turn off UFW?"
  *(Why it fails: Leading question that encourages an insecure shortcut instead of isolating the network layer.)*

* **Effective Prompt (Recommended):**
  > **Role & Environment:** You are a network engineer troubleshooting local HTTP connectivity on Ubuntu 24.04 LTS.  
  > **Goal:** Isolate whether traffic to TCP port 80 is blocked by a missing listener, routing, or UFW rules.  
  > **Evidence:** `ip -br a` shows `ens33 UP 192.168.56.10/24`; `curl -I http://127.0.0.1` returns `HTTP/1.1 200 OK`, but external host requests time out.  
  > **Constraints:** Keep UFW active at all times. Provide read-only inspection commands first, followed by the narrowest possible UFW rule if needed.  
  > **Output Format:** Step-by-step verification commands and expected outputs.

---

### Example D: Auditing a Suspicious AI-Suggested Command

* **Verification Prompt (Recommended):**
  > "Before I run `sudo find /var/www/html -type f -exec chmod 644 {} +` on Ubuntu 24.04, break down every argument and flag, state what files are affected, and warn me of any unintended side effects if run in the wrong directory."

---

## 3. Data Sanitization Checklist Before Pasting Logs
Always scrub the following items before sending logs or configs to any external AI tool:
* [ ] Passwords, API keys, bearer tokens, and database connection strings (`<REDACTED_SECRET>`)
* [ ] Private SSH/TLS keys (`-----BEGIN ... PRIVATE KEY-----`)
* [ ] Public IP addresses, internal hostnames, and customer usernames (`<SERVER_IP>`, `<USER>`)
* [ ] Proprietary source code or confidential business records
