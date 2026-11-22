# ChatGPT Guide for IT Technicians & Students
**02-Artificial-Intelligence | Alijó IT Workshops**

---

## 1. Overview & Best Use Cases in IT Labs
ChatGPT is an effective conversational assistant for rapidly structuring troubleshooting plans, explaining unfamiliar Linux flags, translating error logs into plain language, and drafting shell or Python diagnostic scripts.

### Recommended IT Lab Tasks
* Explaining multi-line `systemd`, `journalctl`, or `nginx` error messages.
* Generating step-by-step diagnostic checklists ordered from read-only checks to safe fixes.
* Reviewing short Python or Bash scripts for syntax errors, logic bugs, and missing error handling.
* Converting raw terminal findings into structured incident summaries.

---

## 2. Recommended Workflow in Workshops
1. **Collect Local Evidence First:** Gather exact terminal output (`systemctl status`, `journalctl -xe`, `ip a`, or script tracebacks) before opening ChatGPT.
2. **Sanitize Sensitive Data:** Replace real IP addresses, domain names, usernames, passwords, and API keys with placeholders (e.g., `<SERVER_IP>`, `<REDACTED_TOKEN>`).
3. **Use Structured Context:** Specify your exact OS version (`Ubuntu 24.04 LTS`), target service, and safety constraints (*"Give read-only commands first; do not disable UFW or use chmod 777"*).
4. **Verify Every Command:** Check all suggested flags with `man <command>` or `<command> --help` in your Ubuntu VM before running anything.

---

## 3. Strengths & Watch-Outs for IT Troubleshooting

| Strengths | Common Watch-Outs / Failure Modes |
| :--- | :--- |
| Fast at breaking down unfamiliar error codes and stack traces. | May default to overly permissive quick fixes (`chmod 777`, `ufw disable`, `sudo rm -rf`) unless explicitly constrained. |
| Good at refactoring messy Bash/Python snippets into cleaner functions. | Can invent non-existent CLI flags for niche Linux utilities or older package versions. |
| Helpful for generating test cases and edge-case checklists. | Assumes default paths (`/var/www/html`, `/etc/nginx/`) that may differ from your lab setup. |

---

## 4. Quick Prompt Template for ChatGPT

```text
Role: You are a senior Linux system administrator assisting with an Ubuntu 24.04 lab environment.
Problem: [Describe symptom in 1-2 sentences]
Exact Evidence:
[Paste sanitized log lines or command output]

Constraints:
- Start with read-only diagnostic commands only.
- Explain what every command and flag does before suggesting changes.
- Follow least-privilege security practices (never suggest chmod 777 or disabling the firewall).
```
