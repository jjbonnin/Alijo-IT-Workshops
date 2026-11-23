# Teacher Resources — Alijó IT Workshops

> **🛑 STRICTLY CONFIDENTIAL - INSTRUCTORS ONLY 🛑**
>
> This directory contains solution keys, fault-injection scripts, expected diagnoses, and assessment rubrics for the Alijó IT Workshops. **Do not share this folder with students.** If students are given read access to the main repository, this `Teacher-Resources` folder must be removed and hosted in a separate, private repository.

## Overview

This centralized directory provides instructors with everything needed to deploy, manage, and grade the workshops. The resources are divided by workshop:

### [Workshop 1: IT Troubleshooting Challenge](./Workshop-1-IT-Troubleshooting-Challenge/)
* `Teacher-Guide.md`: Step-by-step fault injection commands, recovery procedures, and session pacing.
* `Assessment-Rubric.md`: The grading framework for evaluating student incident reports and methodology.
* `Expected-Diagnoses.md`: A quick-reference cheat sheet detailing the root cause for all 6 incidents.

### [Workshop 2: AI as an IT Technician Assistant](./Workshop-2-AI-IT-Technician-Assistant/)
* `Teacher-Guide.md`: Session pacing, AI verification rules, and instructor facilitation notes.
* `Assessment-Rubric.md`: Grading framework for evidence-first prompting, pre-execution audits, and technical execution.
* `Solutions-and-Setup/`: Reference prompt templates, debugged `diagnostic_script.py` solution, and Scenario 03 safety trap answers.

### [Workshop 3: Build and Configure a Network](./Workshop-3-Build-and-Configure-Network/)
* `Teacher-Guide.md`: 180-minute pacing plan for design, Packet Tracer simulation, physical Ethernet lab, and troubleshooting.
* `Assessment-Rubric.md`: 100-point rubric covering IPv4 design, Packet Tracer, physical lab safety, environment comparison, and fault resolution.
* `Solutions-and-Setup/`: Reference topology and IPv4 plan (`Reference-Topology-and-IP-Plan.md`), physical server setup (`Server-Service-Setup.md`), and fault injection/recovery keys (`Fault-Injection-and-Recovery.md`).

### [Workshop 4: Linux Server Administration](./Workshop-4-Linux-Server-Administration/)
* `Instructor-Setup-Guide.md`: Golden Ubuntu VM baseline preparation and automated 5-fault injection script (`INC-401`).
* `Answer-Key.md`: Reference solutions for user/group permissions, `systemd` reload vs. restart, `cron` scheduling, and final challenge remediation.
* `Assessment-Rubric.md`: 100-point competency rubric with automatic security penalties.
* `Presentation-Outline.md`: 9-slide instructor deck outline covering all lab modules and safety rules.

## General Instructor Guidelines

1. **Environment Preparation:** Always review the instructor guide for each workshop at least one day before the lab. Ensure VM baselines and snapshots are correctly configured.
2. **Controlled Execution:** For fault-injection labs, ensure students have documented their baseline *before* you run the break scripts.
3. **Assessment Focus:** Grade students on their adherence to the methodology (evidence gathering, hypothesis testing, and pre-execution safety checks) rather than just achieving the final fix. Use the provided rubrics to maintain consistency.
