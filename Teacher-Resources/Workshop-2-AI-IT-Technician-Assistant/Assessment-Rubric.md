# Assessment Rubric — Workshop 2: AI as an IT Technician Assistant
**Total Score: 100 Points | Passing Threshold: 70 Points**

> **Shared Standard:** This rubric aligns with the [Shared Assessment Framework](../../00-Shared-Resources/Rubrics/Shared-Assessment-Framework.md).

---

## Evaluation Matrix

| Criterion & Weight | Exemplary (90–100%) | Proficient (75–89%) | Developing (60–74%) | Incomplete / Unsatisfactory (< 60%) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Evidence-First & Prompt Quality**<br>*(25 Points)* | Always collects and inspects raw local logs/errors before consulting AI. Uses the 5-part prompt structure consistently with clear OS context, exact outputs, and safety constraints; zero credentials or sensitive host data leaked. *(23–25 pts)* | Collects local evidence before prompting in most scenarios; prompts include OS context and error text, though constraints or output formatting could be tighter. *(19–22 pts)* | Occasionally consults AI before gathering local evidence; prompts are vague or summarize errors instead of pasting exact logs. *(15–18 pts)* | Relies on vague prompts without local diagnostics, or pastes sensitive credentials/keys into prompts. *(0–14 pts)* |
| **2. Pre-Execution Audit & Critical Thinking**<br>*(30 Points)* | Rigorously audits every AI suggestion using `man`, `--help`, and code inspection before execution. Identifies all 3 dangerous commands in Scenario 03 with accurate risk explanations and production-grade safe replacements. *(27–30 pts)* | Audits AI commands before running them and catches most risks; identifies all 3 traps in Scenario 03 with minor gaps in risk detail or safe replacement flags. *(23–26 pts)* | Performs superficial checks on AI outputs; misses subtle logic flaws or partially explains the risks in Scenario 03. *(18–22 pts)* | Blindly copy-pastes AI commands without verification, or executes destructive/insecure commands on the VM. *(0–17 pts)* |
| **3. Technical Execution & Verification**<br>*(25 Points)* | Accurately diagnoses the failing service in Scenario 01, fixes all 4 bugs in `diagnostic_script.py` cleanly, and proves every fix with real terminal outputs in the Ubuntu VM. *(23–25 pts)* | Resolves Scenarios 01 and 02 with minor instructor coaching; script executes properly and verification outputs are documented. *(19–22 pts)* | Partially resolves Scenarios 01 and 02; script still contains minor logic bugs or lacks complete terminal verification evidence. *(15–18 pts)* | Fails to diagnose the service issue or produce a working diagnostic script; lacks terminal verification. *(0–14 pts)* |
| **4. Documentation, Teamwork & Lab Hygiene**<br>*(20 Points)* | `Prompt-and-Results-Record.md` and `Final-Report-Template.md` are thorough, well-structured, and complete; team rotates roles effectively and restores the VM baseline snapshot cleanly. *(18–20 pts)* | Both worksheets are completed with clear prompts, outputs, and reflections; roles are shared and VM is left clean. *(15–17 pts)* | Worksheets are incomplete or missing exact prompts/terminal evidence; uneven role participation. *(12–14 pts)* | Missing worksheets, unverified claims, or VM left broken/unrestored. *(0–11 pts)* |

---

## Automatic Safety Deductions
* **-15 Points:** Executing any of the three prohibited commands from Scenario 03 (`chmod -R 777 /var/www/html`, `ufw disable`, `rm -rf /var/log/*`) on the VM.
* **-10 Points:** Pasting real passwords, SSH private keys, or API tokens into an external AI assistant prompt.
