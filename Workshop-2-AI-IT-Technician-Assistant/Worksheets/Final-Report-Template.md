# Final Technical Report — Workshop 2: AI as an IT Technician Assistant
*(Complete this final report at the end of the lab session using your team's verified findings)*

> **Reference Standard:** This report follows the [Technical Incident Report Base Template](../../00-Shared-Resources/Templates/Incident-Report-Base-Template.md) adapted for AI-assisted troubleshooting and verification.

---

## 1. Team & Environment Details
* **Team Name:** 
* **Team Members & Roles:**
  * Team Coordinator: 
  * Prompt Engineer: 
  * Lab Technician: 
  * Verification Auditor: 
  * Reporter: 
* **Date:** 
* **AI Assistant(s) Used:** 
* **Lab Environment (VM OS & Version):** 

---

## 2. Executive Summary
*(Provide a 3–5 sentence overview of the three challenges completed, how AI was used, and the most important lesson learned about verifying AI outputs.)*

---

## 3. Summary of Scenarios & Verified Outcomes

### Scenario 01: Log Analysis & Failing Service Diagnosis
* **Confirmed Root Cause:** 
* **Most Effective Prompt Strategy Used:** 
* **AI Accuracy Assessment:** *(Did the AI identify the real cause on the first try, or did it require follow-up prompts?)*
* **Verification Evidence:** *(Summary of the exact command/output that proved the cause on the Ubuntu VM)*

### Scenario 02: Debugging `diagnostic_script.py`
* **Bugs Identified in Original Script:** 
* **AI Contribution vs. Team Audit:** *(Which bugs did the AI catch, and what did your Verification Auditor have to fix or refine?)*
* **Verification Evidence:** *(Confirm the script ran cleanly without errors and reported accurate system metrics)*

### Scenario 03: AI Audit & Critical Thinking Challenge (Spot the Trap!)
* **Summary of Dangerous AI Suggestions Rejected:**
  1. `sudo chmod -R 777 /var/www/html` — *Why rejected & safe replacement:* 
  2. `sudo ufw disable` — *Why rejected & safe replacement:* 
  3. `sudo rm -rf /var/log/*` — *Why rejected & safe replacement:* 

---

## 4. Reflection on Responsible AI Use in IT
* **1. Best Prompting Practice:** *(What single change to your prompts improved AI responses the most?)*
* **2. Biggest AI Pitfall Observed:** *(What mistake, hallucination, or risky shortcut did the AI produce during the session?)*
* **3. Verification Rule for Future Work:** *(State one concrete verification habit your team will always apply before executing AI-generated commands.)*

---

## 5. Submission Checklist
* [ ] All 3 scenarios documented in `Prompt-and-Results-Record.md`.
* [ ] Exact prompts and real VM terminal outputs included as evidence.
* [ ] No destructive or unverified commands executed on the host system.
* [ ] Ubuntu VM restored or left in a clean state.
