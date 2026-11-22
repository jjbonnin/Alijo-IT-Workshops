# Student Scenario Cards
**Workshop 2: AI as an IT Technician Assistant**

> **Instructions:** Work through each scenario in order using the **5-Step AI-Assisted IT Workflow**. You must collect local evidence first, craft a structured prompt, audit the AI response before executing any command, and record all prompts and verification outputs in `Prompt-and-Results-Record.md`.

---

## Scenario 01: Log Analysis & Failing Service Diagnosis
* **Role:** Junior IT Support Technician
* **Context:** A local web/application service on the Ubuntu VM is failing to start or throwing errors in the system logs (check `/var/log/syslog`, `journalctl`, or the sample log provided in `Assets/sample-service.log`).
* **Your Task:**
  1. Inspect the log file and service status on your Ubuntu VM **before** opening the AI tool.
  2. Build a structured 5-part prompt including the exact error lines and your OS environment.
  3. Ask the AI to identify the 2 most likely root causes and the safest diagnostic commands to verify each one.
  4. Verify the AI's explanation against the actual system configuration on the VM.
* **Deliverable:** Exact prompt used, AI response summary, commands run to verify the cause, and confirmed root cause.

---

## Scenario 02: Debugging a Broken Administrative Script (`diagnostic_script.py`)
* **Role:** Systems Automation Technician
* **Context:** A colleague left a Python 3 monitoring script at `Assets/diagnostic_script.py` meant to check disk space, verify network connectivity, and inspect service status—but it crashes or produces misleading results.
* **Your Task:**
  1. Run `python3 Assets/diagnostic_script.py` inside the VM first to observe the exact error messages and behavior.
  2. Prompt the AI to review the script, explain every syntax error, logic flaw, or unsafe shell call, and propose a corrected version.
  3. Audit every line of the AI's proposed code (check imports, shell commands, thresholds, and exit codes) before saving or running it.
  4. Test the fixed script in the VM and verify that all checks report accurate results.
* **Deliverable:** Initial error output, prompt used, list of bugs caught (by AI and by your team), and terminal output of the verified working script.

---

## Scenario 03: AI Audit & Critical Thinking Challenge (Spot the Trap!)
* **Role:** Senior Verification Auditor
* **Context:** An impatient technician asked an AI *"How do I fix permission denied errors on `/var/www/html` and make my app run fast on Ubuntu?"* and received the following AI-generated fix:
  ```bash
  sudo chmod -R 777 /var/www/html
  sudo ufw disable
  sudo rm -rf /var/log/*

Your Task:

DO NOT run any of these commands on your VM.

Analyze each of the three commands using man pages, --help, and security best practices (you may also use AI to cross-check specific risks, then verify independently).

Identify the exact security or operational damage each command would cause in a real Ubuntu environment.

Propose safe, production-grade replacement commands for each legitimate administrative goal (proper web directory permissions, firewall rule for HTTP/HTTPS, and safe log rotation/cleanup).

Deliverable: Detailed risk breakdown for all 3 flawed commands and verified safe alternative commands.
