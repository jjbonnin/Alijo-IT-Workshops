# Instructor Guide — Workshop 2: AI as an IT Technician Assistant
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

> **Shared Lab Reference:** This guide integrates with the [Shared Instructor Lab Playbook](../../00-Shared-Resources/Instructor-Lab-Playbook.md) and the [VM Snapshots & Recovery Guide](../../00-Shared-Resources/Virtualization-Guides/Snapshots-and-Recovery.md).

---

## 1. Session Objectives & Pedagogical Focus
In this 3-hour workshop, students learn how to use AI assistants as a force multiplier for IT troubleshooting and scripting while maintaining strict human oversight. The core goal is to break the habit of "blind copy-pasting" by enforcing a mandatory **Evidence → Prompt → Audit → Sandbox Test → Document** workflow.

---

## 2. Pre-Workshop Lab Setup Checklist
Before students enter the lab, verify the following on every workstation:
* [ ] Ubuntu Desktop VM boots cleanly and has the `BASELINE – BEFORE WORKSHOP` snapshot created.
* [ ] Workshop 2 files (`Assets/diagnostic_script.py` and `Assets/sample-service.log`) are accessible inside the VM or shared folder.
* [ ] Browser access to the approved AI assistant is working on each team station.
* [ ] **Scenario 01 Live Option (Optional):** If you want teams to inspect a live failing service instead of (or in addition to) `Assets/sample-service.log`, start a lightweight Python HTTP listener on port `80` (`sudo python3 -m http.server 80 &`) and leave `nginx` installed in a stopped/failing state so students observe a genuine `Address already in use` conflict.
* [ ] Confirm students understand that **Scenario 03 commands must never be executed**.

---

## 3. Instructor Pacing & Facilitation Plan (180 Minutes)

| Time Block | Duration | Phase | Instructor Actions & Checkpoints |
| :--- | :--- | :--- | :--- |
| **00:00–00:15** | 15 min | **Welcome & AI Safety Briefing** | Introduce workshop goals, assign the 5 team roles, and emphasize the Golden Rule (zero blind execution; no credentials/keys in prompts). |
| **00:15–00:35** | 20 min | **5-Part Prompting & Audit Workflow** | Walk through `Prompting-Guidelines.md` and demonstrate one weak vs. structured prompt live. Highlight the Red-Flag Checklist. |
| **00:35–00:55** | 20 min | **VM Baseline Check** | Have teams verify their VM snapshot, inspect `Assets/`, and record baseline system details in `Prompt-and-Results-Record.md`. |
| **00:55–01:55** | 60 min | **Challenges 1 & 2 (Logs & Script Debugging)** | Circulate among teams. **Checkpoint:** Refuse to help teams that ask AI before collecting local evidence first. Remind teams to rotate roles after Scenario 01. |
| **01:55–02:20** | 25 min | **Challenge 3 (Spot the Trap!)** | Monitor closely to ensure no team runs `chmod 777`, `ufw disable`, or `rm -rf /var/log/*`. Require `man` / `--help` verification for every alternative command. |
| **02:20–02:40** | 20 min | **Final Verification & Reporting** | Ensure teams re-test `diagnostic_script.py` end-to-end and complete `Final-Report-Template.md`. |
| **02:40–03:00** | 20 min | **Team Debriefs & Evaluation** | Ask each team to share: (1) their best prompt, (2) one AI flaw/risk they caught, and (3) how they verified their solution. |

---

## 4. Common Student Pitfalls & Coaching Interventions
* **Pitfall 1: Asking AI before reading the error.**
  * *Intervention:* Ask the team to show you their raw terminal output or log lines before looking at their AI chat window.
* **Pitfall 2: Accepting the AI's rewritten script without checking logic.**
  * *Intervention:* Ask the *Verification Auditor* to explain what `shutil.disk_usage()` or `systemctl is-active` exit codes actually return.
* **Pitfall 3: Running `ping` without `-c` in `diagnostic_script.py`.**
  * *Intervention:* On Linux, `ping <host>` runs infinitely until interrupted (`Ctrl+C`), hanging the script. Check if the AI or the student caught this!
* **Pitfall 4: Pasting sensitive host info into the prompt.**
  * *Intervention:* Remind students to sanitize hostnames, IPs, or usernames when working with external AI services.

---

## 5. End-of-Session Cleanup
1. Collect each team's completed `Prompt-and-Results-Record.md` and `Final-Report-Template.md`.
2. Instruct teams to power off their Ubuntu VM and restore the `BASELINE – BEFORE WORKSHOP` snapshot so the workstation is ready for Workshop 3.
