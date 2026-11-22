# Student Workbook — Workshop 2: AI as an IT Technician Assistant
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

---

## 1. Workshop Overview
**Aim:** Use Artificial Intelligence (AI) tools responsibly and effectively as a technical assistant to interpret logs, debug scripts, and evaluate administrative solutions—always validating every recommendation in a safe test environment before applying changes.

By the end of this workshop, you will be able to:
* Write clear, structured, context-rich prompts for technical IT tasks.
* Use AI to interpret system logs, error messages, and diagnostic command outputs.
* Generate and debug basic administrative scripts (Bash / Python) with AI assistance.
* Detect AI hallucinations, invented command flags, and unsafe recommendations.
* Verify AI-proposed fixes inside an isolated Ubuntu virtual machine before trusting them.
* Document prompts, AI responses, verification checks, and human corrections clearly.

---

## 2. Materials and Preparation

| Area | Materials / Requirements |
| :--- | :--- |
| **Hardware** | One PC per team of 4–5 students; keyboard, mouse, and display. |
| **Virtualisation** | Oracle VM VirtualBox installed and tested. |
| **Virtual Machine** | Ubuntu Desktop VM with a clean snapshot taken before the workshop. |
| **AI Access** | Approved AI chat assistant accessible via browser on the workstation. |
| **Student Documents** | This workbook, Prompting Guidelines, Scenario Cards, Prompt & Results Record, and Final Report Template. |
| **Lab Assets** | Sample log files and `diagnostic_script.py` located in the lab directory. |

### Recommended VM Baseline & Safety Rules
Before starting any AI-assisted tasks, confirm the following baseline setup with your team and instructor:
* The Ubuntu Desktop VM boots properly and you can log in with the lab account.
* A clean snapshot named **`BASELINE – BEFORE WORKSHOP`** exists in VirtualBox (see the [VM Snapshots & Recovery Guide](../../../00-Shared-Resources/Virtualization-Guides/Snapshots-and-Recovery.md)).
* **Zero Blind Execution:** Never paste an AI-generated command into your terminal without reading and understanding every flag and target path.
* **Data Privacy:** Never paste real passwords, SSH private keys, API tokens, or institutional network credentials into any AI tool.
* **Scope Boundary:** Execute all test scripts and commands strictly inside your disposable Ubuntu VM.

---

## 3. Three-Hour Schedule

| Duration | Activity | Expected Outcome |
| :--- | :--- | :--- |
| **15 min** | Welcome, AI safety briefing, and team roles | Understand workshop goals, AI risks, and team responsibilities. |
| **20 min** | Structured prompting & verification workflow | Learn the 5-part technical prompt formula and verification loop. |
| **20 min** | Initial VM inspection & baseline check | Record VM system details and confirm access to lab sample files. |
| **60 min** | AI-assisted diagnostic & scripting rounds (Challenges 1–2) | Analyze system logs and debug `diagnostic_script.py` using AI + verification. |
| **25 min** | AI audit & critical thinking challenge (Challenge 3) | Identify flaws, hallucinations, or unsafe advice in an AI response. |
| **20 min** | Verification & technical documentation | Re-test scripts/commands and complete the Final Report. |
| **20 min** | Team debriefs and evaluation | Present prompts, AI errors caught, and verified solutions. |

**Total: 180 minutes.** Keep prompt iterations focused so your team has sufficient time to verify outputs on the command line and document evidence.

---

## 4. Team Organisation

| Role | Main Responsibilities |
| :--- | :--- |
| **Team Coordinator** | Keeps the team on schedule, reads the scenario card, and ensures decisions are agreed upon. |
| **Prompt Engineer** | Writes and refines structured prompts based on technical evidence collected by the team. |
| **Lab Technician** | Runs diagnostic commands and tests AI-suggested scripts inside the Ubuntu VM. |
| **Verification Auditor** | Critically reviews every AI output for errors, dangerous flags, or missing edge cases before execution. |
| **Reporter** *(for teams of five)* | Records prompts, AI outputs, and test evidence into the final report and presents findings. |

* **Teams of four:** Combine the *Reporter* and *Team Coordinator* roles.
* **Role rotation:** Rotate the *Prompt Engineer* and *Lab Technician* roles between challenges so every member practices both prompting and terminal verification.

---

## 5. The 5-Step AI-Assisted IT Workflow

Follow this cycle strictly for every scenario in the workshop:

1. **Collect Real Evidence First:** Inspect the system, log file, or script yourself before asking the AI anything. Never ask AI to guess without real error output.
2. **Build a Structured Prompt:** Provide clear context (OS version, goal, exact error message/code, and safety constraints) following `Prompting-Guidelines.md`.
3. **Audit the AI Response:** Before running anything, check every suggested command using `--help`, `man`, or syntax inspection. Look for destructive flags (`rm -rf`, `chmod 777`, wrong paths).
4. **Test in a Controlled Environment:** Run the approved command or script inside your Ubuntu VM and observe the actual output.
5. **Refine & Document:** If the test fails or reveals edge cases, feed the new error back to the AI, re-verify, and record both the prompt and final verified evidence.
