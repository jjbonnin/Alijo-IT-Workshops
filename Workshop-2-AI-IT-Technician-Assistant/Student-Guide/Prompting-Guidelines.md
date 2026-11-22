# Technical Prompting Guidelines
**Workshop 2: AI as an IT Technician Assistant**

> **Core Principle:** Vague prompts produce vague—and sometimes dangerous—answers. Always give the AI structured technical context, real command outputs, and strict safety boundaries.

---

## 1. The 5-Part Technical Prompt Formula

Whenever you ask an AI assistant for help with an IT problem, build your prompt using these five elements:

1. **Role & Environment:** Define the operating system, version, and technical context.
   * *Example:* `"You are a Linux system administrator helping me troubleshoot an Ubuntu 24.04 Desktop VM running in VirtualBox."`
2. **Clear Goal:** State exactly what you want to achieve or understand.
   * *Example:* `"Explain what is causing the service failure shown in the log below and suggest how to diagnose it further."`
3. **Real Evidence (Logs / Code / Outputs):** Paste the exact error message, log snippet, or script lines—never summarize them in your own words.
   * *Example:* `"Here is the output of systemctl status nginx and the last 20 lines of /var/log/nginx/error.log: [paste raw output]"`
4. **Constraints & Safety Rules:** Tell the AI what *not* to do (e.g., avoid destructive commands, explain every flag).
   * *Example:* `"Do not suggest disabling security features or using chmod 777. Explain every command and flag you recommend."`
5. **Expected Output Format:** Specify how you want the answer structured so your team can verify it quickly.
   * *Example:* `"List the 2 most likely root causes, the diagnostic command to confirm each one, and the safest fix."`

---

## 2. Weak Prompts vs. Effective Prompts

| Task | Weak Prompt (Avoid) | Effective Prompt (Use This) |
| :--- | :--- | :--- |
| **Log Analysis** | `"My web server isn't working, how do I fix it?"` | `"On Ubuntu 24.04, Apache fails to start with the error 'Address already in use: AH00072: make_sock: could not bind to address [::]:80'. Which diagnostic commands confirm which process holds port 80, and how do I resolve it safely?"` |
| **Script Debugging** | `"Fix this python script: [code]"` | `"Review this Python 3 script intended to check disk usage and service status on Ubuntu. Identify any syntax errors, logic bugs, or unsafe assumptions, explain why each occurs, and provide a corrected version with comments."` |
| **Command Explanation** | `"How do I find big files in Linux?"` | `"Show me a read-only Linux command to find files larger than 100 MB inside /var/log on Ubuntu without modifying or deleting anything, and explain each flag used."` |

---

## 3. Red-Flag Checklist (Before Running Any AI Suggestion)

Before your **Lab Technician** executes any AI-suggested command or script, the **Verification Auditor** must check for these common AI failure modes:

* **Invented Flags or Non-Existent Packages:** Does `--help` or `man <command>` confirm every flag suggested by the AI actually exists in this Ubuntu version?
* **Destructive Operations:** Does the command contain `rm -rf`, `dd`, `mkfs`, `>`, or recursive ownership/permission changes (`chmod -R 777`, `chown -R`) on system directories?
* **Hardcoded Placeholders:** Did the AI leave dummy paths (`/path/to/file`), fake IPs (`192.0.2.1`), or generic interface names (`eth0` instead of `enp0s3`)?
* **Security Shortcuts:** Does the AI recommend disabling firewalls (`ufw disable`), running scripts as `root` unnecessarily, or exposing sensitive services?
* **Data Leak Check:** Did your team accidentally paste real passwords, private keys, or host network details into the prompt?
