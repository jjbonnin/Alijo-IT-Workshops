# Workshop 1: IT Troubleshooting Challenge

*Practical Approaches to IT Projects and Problem-Solving* | **Alijó IT Workshops**

| Format | Duration | Team Size | Target Environment |
| :--- | :--- | :--- | :--- |
| Hands-on practical lab | 3 hours (180 minutes) | 4–5 students | Ubuntu Desktop VM (Oracle VM VirtualBox) |

---

## Overview

Welcome to **Workshop 1: IT Troubleshooting Challenge**. In this hands-on lab, your team will act as IT support technicians tasked with diagnosing, resolving, and documenting real-world system and network incidents inside a controlled virtual machine environment.

Rather than guessing or applying random fixes, you will follow a structured, repeatable 7-step troubleshooting methodology—collecting evidence, testing hypotheses, implementing safe changes, and verifying results.

### Learning Objectives

By the end of this workshop, you will be able to:
* Follow a repeatable troubleshooting process instead of guessing.
* Collect relevant diagnostic information and distinguish symptoms from root causes.
* Use foundational Linux command-line tools in an Ubuntu Desktop virtual machine.
* Apply controlled, reversible fixes and verify that affected services or applications work properly.
* Record actions, outputs, and evidence in a clear, reproducible technical incident report.
* Collaborate effectively within defined technical team roles and communicate findings.

---

## Prerequisites & Environment Setup

Before starting the workshop, ensure your workstation meets the baseline requirements:
1. **Host & Virtualization:** A workstation with Oracle VM VirtualBox installed and tested.
2. **Virtual Machine:** A pre-configured Ubuntu Desktop VM with a clean baseline snapshot (`BASELINE – BEFORE WORKSHOP`).
3. **Network Access:** Working local network or internet access routed safely to the VM.

> **Need help setting up VirtualBox or managing snapshots?**  
> Refer to the shared guides in the repository:
> * [VirtualBox Setup Guide](../../00-Shared-Resources/Virtualization-Guides/VirtualBox-Setup.md)
> * [Snapshots and Recovery Guide](../../00-Shared-Resources/Virtualization-Guides/Snapshots-and-Recovery.md)

---

## Repository Contents (Student Materials)

All student-facing guides, checklists, and templates for this workshop are organized in this directory:

* **Student Guides (`Student-Guide/`)**
  * [`Student-Workbook.md`](Student-Guide/Student-Workbook.md) — Complete workshop manual covering the schedule, team roles, 7-step methodology, and Ubuntu command quick reference.
  * [`Incident-Cards.md`](Student-Guide/Incident-Cards.md) — Detailed symptoms, tasks, suggested commands, and safety rules for Incidents 01–05.
  * [`Diagnostic-Checklist.md`](Student-Guide/Diagnostic-Checklist.md) — Step-by-step verification checklist to follow during every incident.
* **Worksheets & Templates (`Worksheets/`)**
  * [`Incident-Log.md`](Worksheets/Incident-Log.md) — Structured log sheet (complete one copy per incident).
  * [`Final-Report-Template.md`](Worksheets/Final-Report-Template.md) — Template for your team's final technical incident report and 2–3 minute presentation outline.
* **Lab Assets (`Assets/`)**
  * [`Lab-Sample-Files/`](Assets/Lab-Sample-Files/) — Practice files and scripts used during specific troubleshooting scenarios.

---

## Workshop Safety Rules

* **Stay inside the sandbox:** Perform all diagnostic commands and configuration changes strictly inside your disposable Ubuntu VM.
* **Protect shared infrastructure:** Never alter host PC settings, physical routers, DHCP servers, or school network configurations.
* **Ask before escalating privileges:** Consult your instructor before running `sudo` to modify system configurations.
* **Avoid destructive shortcuts:** Never use broad permission overrides (such as `chmod 777`) or delete unfamiliar system files.
