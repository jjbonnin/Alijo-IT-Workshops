# Teacher Guide — Workshop 1: IT Troubleshooting Challenge
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

> **Confidentiality Notice:** This document is intended exclusively for instructors. Keep it inside `Teacher-Resources/Workshop-1-IT-Troubleshooting-Challenge/` and do not distribute it to students.

---

## 1. Workshop Overview & Objectives

* **Format:** Hands-on practical lab (180 minutes / 3 hours)
* **Team Size:** 4–5 students per team
* **Core Mission:** Guide students to resolve realistic Ubuntu Linux incidents using a repeatable 7-step diagnostic methodology instead of random guessing.

### Learning Outcomes
By the end of the session, students must demonstrate they can:
1. Separate observable **symptoms** from underlying **root causes**.
2. Gather baseline and diagnostic evidence before modifying system settings.
3. Execute safe, reversible fixes with instructor approval.
4. Prove resolution through repeatable verification tests and structured documentation.

---

## 2. Pre-Workshop Environment Preparation

Complete these checks on every student workstation before the session begins:

- [ ] **VirtualBox & VM:** Verify Oracle VM VirtualBox launches properly and the Ubuntu Desktop VM boots without errors.
- [ ] **Lab Credentials:** Confirm the student lab account logs in smoothly (never hardcode passwords in shared files or screenshots).
- [ ] **Clean Baseline Snapshot:** Create a snapshot named `BASELINE – BEFORE WORKSHOP` with working network and DNS connectivity.
- [ ] **Incident 04 Target File:** Pre-create `~/lab-files/report-generator.sh` on the VM (permissions will be stripped when assigning Incident 04).
- [ ] **Incident 05 Target App:** Place the clean executable script at `/opt/lab-apps/app-monitor.py` (`chmod +x`) and ensure `/tmp/it-monitor` does not exist.
- [ ] **Printed / Digital Handouts:** Ensure teams have access to `Student-Workbook.md`, `Incident-Cards.md`, `Diagnostic-Checklist.md`, `Incident-Log.md`, and `Final-Report-Template.md`.

### Safety & Scope Boundaries
* All changes and fault injections must occur strictly inside the **disposable Ubuntu VM**.
* Students must **never** alter host OS settings, school LAN cables, routers, or DHCP/DNS servers.
* Any use of `sudo` or system-level modification requires prior instructor sign-off.

---

## 3. Session Pacing & Facilitation Guide (180 Minutes)

### Phase 1: Welcome, Challenge Briefing & Team Roles (`00:00 – 00:15` | 15 min)
* **Instructor Actions:** Introduce the scenario, explain lab safety rules, and organize students into teams of 4–5. Have teams assign roles: *Team Coordinator*, *Lead Technician*, *Evidence Recorder*, *Verifier/Tester*, and *Reporter*.
* **Facilitation Tip:** Remind teams of four to merge the *Coordinator* and *Reporter* roles. Emphasize that jumping straight into terminal commands without team consensus violates the lab protocol.

### Phase 2: Troubleshooting Methodology (`00:15 – 00:35` | 20 min)
* **Instructor Actions:** Walk through the 7-step workflow:
  1. *Identify* → 2. *Gather evidence* → 3. *Form hypothesis* → 4. *Test hypothesis* → 5. *Implement fix* → 6. *Verify* → 7. *Document*.
* **Facilitation Tip:** Highlight the difference between a symptom (*"The browser won't load pages"*) and a root cause (*"DNS resolution is pointing to an invalid server"*). Clarify that writing *"it works now"* is insufficient—raw CLI output is required as proof.

### Phase 3: Initial Inspection & Baseline Collection (`00:35 – 00:55` | 20 min)
* **Instructor Actions:** Instruct teams to boot their VMs, verify the `BASELINE – BEFORE WORKSHOP` snapshot, and record healthy system parameters (`whoami`, `hostname`, `ip address`, `ip route`, `resolvectl status`).
* **Facilitation Tip:** Circulate around the lab to verify every team has recorded their working IP address and default gateway. They will rely on this baseline during Incident 01 and the Surprise Incident.

### Phase 4: Incident-Solving Rounds (`00:55 – 01:55` | 60 min)
* **Instructor Actions:** Assign 3–4 incident cards per team from Incidents 01–05. Inject the corresponding faults into their VMs using `Solutions-and-Setup/Fault-Injection-and-Recovery.md`.
* **Facilitation Tip:** Act as the approval gatekeeper before any `sudo` fix is executed. Ask the **Lead Technician**: *"What evidence supports your hypothesis?"* Enforce role rotation after every incident so every student practices on the command line.

### Phase 5: Surprise Incident (`01:55 – 02:20` | 25 min)
* **Instructor Actions:** At minute 115, inject Incident 06 (e.g., `sudo ip route del default`) into the VMs and distribute the Surprise Incident brief (see `Solutions-and-Setup/Surprise-Incident-Setup.md`).
* **Facilitation Tip:** Step back and withhold hints unless safety is at risk. Observe whether teams diagnose layer-by-layer (interface → IP → route → gateway → external IP) and compare against their Phase 3 baseline.

### Phase 6: Verification & Technical Documentation (`02:20 – 02:40` | 20 min)
* **Instructor Actions:** Signal the end of active troubleshooting. Have teams perform final regression checks and compile their `Incident-Log.md` entries into `Final-Report-Template.md`.
* **Facilitation Tip:** Remind *Evidence Recorders* and *Reporters* to embed terminal outputs or screenshots directly into each incident section.

### Phase 7: Team Presentations & Evaluation (`02:40 – 03:00` | 20 min)
* **Instructor Actions:** Have each team deliver a 2–3 minute debrief summarizing their toughest incident, the evidence collected, the root cause, and lessons learned.
* **Facilitation Tip:** Score teams using `Assessment-Rubric.md`, prioritizing diagnostic discipline, safe execution, and teamwork over raw speed.

---

## 4. Quick Reference: Reference Documents in Teacher-Resources

* **`Solutions-and-Setup/Fault-Injection-and-Recovery.md`**: Exact `nmcli`, `systemctl`, `chmod`, and file-removal commands to break and restore Incidents 01–06.
* **`Solutions-and-Setup/Surprise-Incident-Setup.md`**: Step-by-step protocol for deploying Incident 06 at minute 115.
* **`Solutions-and-Setup/Expected-Diagnoses.md`**: Instructor cheat sheet mapping symptoms to root causes and expected student commands.
* **`Solutions-and-Setup/app-monitor-annotated.py`**: Line-by-line commented reference of the Python script used in Incident 05.
* **`Assessment-Rubric.md`**: 20-point grading matrix across Methodology, Diagnostics, Resolution, Documentation, and Teamwork.
