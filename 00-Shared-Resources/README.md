# Shared Resources
**Alijó IT Workshops | Cross-Workshop Guides & Templates**

This folder contains reusable documentation, virtualization procedures, and standard reporting templates shared across multiple workshops (Workshops 1–4) to avoid duplication and ensure consistent lab standards.

---

## Contents

### 1. Instructor Facilitation
* **[Instructor-Lab-Playbook.md](./Instructor-Lab-Playbook.md)**
  * A phase-by-phase facilitation roadmap for instructors covering pre-lab setup, 180-minute session pacing, `sudo` approval gates, emergency VM recovery, and final assessment across all workshops.

### 2. Virtualization Guides (`./Virtualization-Guides/`)
* **[VirtualBox-Setup.md](./Virtualization-Guides/VirtualBox-Setup.md)**
  * Baseline VM hardware specifications, isolated network configuration rules (NAT vs. Internal Network), and instructions for simulating physical cable disconnects.
* **[Snapshots-and-Recovery.md](./Virtualization-Guides/Snapshots-and-Recovery.md)**
  * Step-by-step instructions for creating the mandatory `BASELINE – BEFORE WORKSHOP` snapshot before a lab and restoring a broken VM in seconds.

### 3. Standard Templates (`./Templates/`)
* **[Incident-Report-Base-Template.md](./Templates/Incident-Report-Base-Template.md)**
  * The foundational technical report structure used by student teams to document symptoms, baseline state, diagnostic evidence, root causes, and verification checks.

---

## How to Link These Resources in Workshop Guides
When referencing these files from a workshop directory (e.g., `01-Problem-Solving/Workshop-1-IT-Troubleshooting-Challenge/`), use relative Markdown links:

```markdown
* [Shared Instructor Lab Playbook](../../00-Shared-Resources/Instructor-Lab-Playbook.md)
* [VirtualBox Lab Setup Guide](../../00-Shared-Resources/Virtualization-Guides/VirtualBox-Setup.md)
* [VM Snapshots & Recovery Guide](../../00-Shared-Resources/Virtualization-Guides/Snapshots-and-Recovery.md)
* [Technical Incident Report Base Template](../../00-Shared-Resources/Templates/Incident-Report-Base-Template.md)
