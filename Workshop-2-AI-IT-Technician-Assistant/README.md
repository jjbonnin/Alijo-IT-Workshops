# Workshop 2: AI as an IT Technician Assistant

Welcome to Workshop 2! In this hands-on 3-hour lab, you will learn how to use Artificial Intelligence (AI) tools effectively as a support assistant for IT troubleshooting, scripting, and system administration—while rigorously verifying every AI-generated suggestion before execution.

## Aim
Use AI responsibly and effectively as a technical assistant to analyze logs, debug scripts, and propose administrative solutions, always validating outputs in a safe test environment before applying changes.

## Learning Objectives
By the end of this workshop, you will be able to:
* Write structured, context-rich prompts for technical IT scenarios.
* Use AI to interpret system logs, error messages, and unfamiliar command outputs.
* Generate and debug basic administrative scripts (Bash / Python) with AI assistance.
* Identify AI hallucinations, unsafe commands, and incomplete explanations.
* Verify AI-proposed fixes inside an isolated Ubuntu virtual machine before trusting them.
* Document prompts, AI responses, verification tests, and human corrections clearly.

## Workshop Format
* **Duration:** 3 hours (180 minutes)
* **Team Size:** 4–5 students per team
* **Environment:** Ubuntu Desktop virtual machine (Oracle VM VirtualBox) + approved AI assistant access

## Folder Structure
* `Student-Guide/`: Contains the Student Workbook, Prompting Guidelines, and Scenario Cards.
* `Worksheets/`: Contains blank templates for the Prompt & Results Record and the Final Report Template.
* `Assets/`: Contains sample logs and the buggy script (`diagnostic_script.py`) required for the lab challenges.

## Shared Lab Resources
* **[VirtualBox Lab Setup Guide](../../00-Shared-Resources/Virtualization-Guides/VirtualBox-Setup.md):** Baseline VM hardware specifications and isolated network rules.
* **[VM Snapshots & Recovery Guide](../../00-Shared-Resources/Virtualization-Guides/Snapshots-and-Recovery.md):** How to verify or restore the `BASELINE – BEFORE WORKSHOP` snapshot.
* **[Technical Incident Report Base Template](../../00-Shared-Resources/Templates/Incident-Report-Base-Template.md):** Standard reporting structure used across all workshops.
* **[Shared Instructor Lab Playbook](../../00-Shared-Resources/Instructor-Lab-Playbook.md):** General 180-minute facilitation workflow and lab safety boundaries.

## Team Roles
Divide your team into the following roles and rotate them across challenges:
1. **Team Coordinator:** Keeps the team on schedule, manages challenge briefs, and ensures decisions are agreed upon.
2. **Prompt Engineer:** Drafts and refines structured prompts based on team findings.
3. **Lab Technician:** Executes approved commands and tests scripts inside the Ubuntu VM.
4. **Verification Auditor:** Critically inspects AI responses for risks, hallucinations, or missing edge cases.
5. **Reporter** *(for teams of 5)*: Compiles prompts, outputs, and verification evidence into the final report. *(In teams of 4, combine with Team Coordinator).*

## The Golden Rule of AI in IT
> **Never copy-paste an AI-generated command directly into a terminal without understanding what every flag and argument does.** AI is an assistant, not an authority—you remain responsible for every change made to the system.

---
**Safety Note:**
All commands and scripts generated with AI must be tested strictly inside your disposable Ubuntu VM. Never paste confidential credentials, real network maps, or private keys into public AI tools.
