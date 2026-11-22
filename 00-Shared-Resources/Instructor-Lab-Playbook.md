# Instructor Lab Playbook
**Alijó IT Workshops | Cross-Workshop Facilitation & Operations Guide**

> **Purpose:** This playbook defines the standard operational workflow for instructors across all 180-minute hands-on labs (Workshops 1–4). It specifies **when** and **which** shared resources (`00-Shared-Resources/`), student materials, and instructor solutions to use at each stage of a session.

---

## Phase 0: Pre-Workshop Lab Preparation (1–2 Days Before)

* **Resources Used:**
  * [`VirtualBox-Setup.md`](./Virtualization-Guides/VirtualBox-Setup.md)
  * [`Snapshots-and-Recovery.md`](./Virtualization-Guides/Snapshots-and-Recovery.md)
  * Workshop-specific `Teacher-Guide.md` (located in `Teacher-Resources/Workshop-X-.../`)
* **Instructor Actions:**
  1. **Configure Virtual Machines:** Deploy the required VMs (Ubuntu Desktop for Workshops 1 & 2; Ubuntu Server for Workshop 4) using isolated networking (**NAT** or **Internal Network**). Never bridge experimental VMs to the school production LAN.
  2. **Stage Lab Assets:** Place pre-built scripts, log files, or sample applications into their target paths inside the VMs (e.g., `/opt/lab-apps/app-monitor.py` for Workshop 1).
  3. **Capture Clean Baseline:** Verify network, DNS, and services work properly, power off the VM cleanly, and create a VirtualBox snapshot named **`BASELINE – BEFORE WORKSHOP`**.
  4. **Isolate Instructor Solutions:** Ensure `Teacher-Resources/` is **not** accessible on student workstations (store it in a private instructor repository or local drive).

---

## Phase 1: Kickoff, Safety Briefing & Team Roles (`00:00 – 00:35` | 35 min)

* **Resources Used:**
  * Workshop `README.md` & `Student-Guide/Student-Workbook.md`
  * [`Snapshots-and-Recovery.md`](./Virtualization-Guides/Snapshots-and-Recovery.md)
* **Instructor Actions:**
  1. **Briefing & Safety (`00:00 – 00:15`):** Establish hard safety boundaries: all actions stay inside the disposable VM, no touching host network settings or school infrastructure, and `sudo` changes require instructor sign-off.
  2. **Team Formation:** Organize students into teams of 4–5 and assign roles (*Team Coordinator*, *Lead Technician*, *Evidence Recorder*, *Verifier/Tester*, and *Reporter*). Remind teams of 4 to merge *Coordinator* and *Reporter*.
  3. **Methodology & VM Boot (`00:15 – 00:35`):** Review the core workshop methodology (7-step troubleshooting loop, AI prompting rules, network design, or server hardening). Have teams boot their VMs and confirm the `BASELINE – BEFORE WORKSHOP` snapshot is visible in VirtualBox.

---

## Phase 2: Initial Inspection & Baseline Collection (`00:35 – 00:55` | 20 min)

* **Resources Used:**
  * `Student-Guide/Diagnostic-Checklist.md` (Workshop 1)
  * `Worksheets/Incident-Log.md` or `Worksheets/Prompt-and-Results-Record.md`
* **Instructor Actions:**
  1. **Record Healthy State:** Have teams run read-only inspection commands (`whoami`, `hostname`, `ip address`, `ip route`, `resolvectl status`, `df -h`) before any faults or changes occur.
  2. **Room Check:** Circulate around the lab to verify every team has actually written down their working IP address, gateway, and DNS servers. They will need this reference baseline to solve later incidents.

---

## Phase 3: Active Lab & Incident-Solving Rounds (`00:55 – 01:55` | 60 min)

* **Resources Used (Students):**
  * `Student-Guide/Incident-Cards.md` or `Scenario-Cards.md`
  * `Worksheets/Incident-Log.md`
* **Resources Used (Instructor Only):**
  * `Teacher-Resources/Workshop-X-.../Solutions-and-Setup/Fault-Injection-and-Recovery.md`
  * `Teacher-Resources/Workshop-X-.../Solutions-and-Setup/Expected-Diagnoses.md`
  * Annotated reference scripts (e.g., `app-monitor-annotated.py`)
* **Instructor Actions:**
  1. **Inject Faults / Assign Tasks:** Apply the controlled faults for assigned scenarios onto each team's VM.
  2. **Act as the `sudo` Gatekeeper:** When a *Lead Technician* requests approval to apply a fix, inspect their `Incident-Log.md` against `Expected-Diagnoses.md`. Deny changes if they are guessing without diagnostic evidence.
  3. **Enforce Role Rotation:** Ensure teams rotate the *Lead Technician* after each completed task so all students practice on the command line.
  4. **Emergency Recovery:** If a team renders a VM unbootable or hopelessly misconfigured, follow [`Snapshots-and-Recovery.md`](./Virtualization-Guides/Snapshots-and-Recovery.md) to revert to `BASELINE – BEFORE WORKSHOP` in seconds.

---

## Phase 4: Surprise Incident / Capstone Challenge (`01:55 – 02:20` | 25 min)

* **Resources Used (Instructor Only):**
  * `Teacher-Resources/Workshop-X-.../Solutions-and-Setup/Surprise-Incident-Setup.md` (Workshop 1) or `Challenge-3-Correction-Notes.md` (Workshop 2)
* **Resources Used (Students):**
  * Final Incident / Challenge brief
* **Instructor Actions:**
  1. **Deploy Without Warning:** At minute 115, introduce the final challenge (e.g., deleting the default route, disconnecting the virtual cable, or presenting a flawed AI recommendation).
  2. **Observe Under Pressure:** Step back and withhold hints unless safety is at risk. Evaluate whether teams follow structured diagnostics and compare against their Phase 2 baseline.

---

## Phase 5: Verification & Technical Documentation (`02:20 – 02:40` | 20 min)

* **Resources Used:**
  * [`Incident-Report-Base-Template.md`](./Templates/Incident-Report-Base-Template.md)
  * Workshop-specific `Worksheets/Final-Report-Template.md`
* **Instructor Actions:**
  1. **Freeze Terminal Changes:** Signal the end of active troubleshooting and instruct teams to run final regression checks.
  2. **Enforce Evidence Standards:** Remind *Evidence Recorders* and *Reporters* that statements like *"it works now"* are unacceptable—reports must contain raw CLI outputs, log snippets, or screenshots.

---

## Phase 6: Team Debriefs & Rubric Assessment (`02:40 – 03:00` | 20 min)

* **Resources Used (Instructor Only):**
  * `Teacher-Resources/Workshop-X-.../Assessment-Rubric.md`
* **Instructor Actions:**
  1. **Short Presentations:** Have each team present a 2–3 minute summary covering symptoms, evidence collected, root cause, verification, and lessons learned.
  2. **Score with Rubric:** Grade teams using the workshop's `Assessment-Rubric.md`, weighting diagnostic discipline, safety, and collaboration higher than raw completion speed.
