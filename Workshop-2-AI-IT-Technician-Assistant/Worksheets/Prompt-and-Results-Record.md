# Prompt and Results Record
**Workshop 2: AI as an IT Technician Assistant**
*(Complete one record block per scenario during the lab session)*

> **Golden Rule Reminder:** Record the exact prompt you sent, summarize the AI's output, document how your **Verification Auditor** checked it before execution, and paste the real terminal output from your Ubuntu VM.

---

## Team Information
* **Team Name & Members:** 
* **Date:** 
* **AI Tool Used:** 
* **VM Hostname & Ubuntu Version:** 

---

## Scenario 01: Log Analysis & Failing Service Diagnosis

* **Prompt Engineer & Lab Technician (Round 1):** 
* **1. Local Evidence Collected Before Using AI:**
  *(Paste the exact log lines or `systemctl status` output you inspected first)*
  ```text

2. Exact Prompt Sent to AI (5-Part Formula):

Plaintext

3. Summary of AI Response & Proposed Commands:(What did the AI identify as likely root causes, and what commands did it suggest?)

4. Pre-Execution Audit (--help / man / Red-Flag Check):(Did the AI suggest any non-existent flags, risky commands, or wrong paths?)

5. Verification Commands & Real VM Output:

Plaintext

6. Verdict on AI Assistance:

[ ] Accurate and directly helpful

[ ] Partially helpful (required team correction)

[ ] Misleading or unsafe (rejected by team)

Scenario 02: Debugging diagnostic_script.py
Prompt Engineer & Lab Technician (Round 2):

1. Initial Error Output Before Using AI:(Paste the raw error when running python3 Assets/diagnostic_script.py)

Plaintext

2. Exact Prompt Sent to AI:

Plaintext

3. Bugs Identified by AI vs. Bugs Caught by Your Team:(List syntax errors, logic bugs, or unsafe calls found)

4. Code Audit Before Running the Fixed Script:(What did your Verification Auditor check in the AI's proposed Python code?)

5. Final Verified Terminal Output:

Plaintext

6. Verdict on AI Assistance:

[ ] Accurate and directly helpful

[ ] Partially helpful (required team correction)

[ ] Misleading or unsafe (rejected by team)

Scenario 03: AI Audit & Critical Thinking Challenge (Spot the Trap!)
Verification Auditor Lead (Round 3):

1. Risk Analysis of the Three Flawed AI Commands:

sudo chmod -R 777 /var/www/html:

Security / Operational Risk:

Safe Alternative Command:

sudo ufw disable:

Security / Operational Risk:

Safe Alternative Command:

sudo rm -rf /var/log/*:

Security / Operational Risk:

Safe Alternative Command:

2. Verification Method Used (man / --help / AI Cross-Check):(How did your team confirm the flags and safe alternatives?)
