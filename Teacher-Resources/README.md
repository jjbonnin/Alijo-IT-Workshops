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

### [Workshop 2: AI as an IT Technician Assistant](./Workshop-2-AI-Assistant/) *(Pending)*
* Instructor guide for managing AI usage, expected prompt structures, and evaluation criteria for AI-assisted troubleshooting.

### [Workshop 3: Build and Configure a Small Network](./Workshop-3-Network-Infrastructure/) *(Pending)*
* Solution network topologies, expected IP schemes, and configuration answer keys for the simulated/physical network setup.

### [Workshop 4: Linux Server Administration Lab](./Workshop-4-System-Administration/) *(Pending)*
* Automated environment setup scripts, configuration answer keys, and server evaluation checklists.

## General Instructor Guidelines

1. **Environment Preparation:** Always review the `Teacher-Guide.md` for each workshop at least one day before the lab. Ensure VM baselines and snapshots are correctly configured.
2. **Controlled Execution:** For fault-injection labs, ensure students have documented their baseline *before* you run the break scripts.
3. **Assessment Focus:** Grade students on their adherence to the methodology (evidence gathering, hypothesis testing) rather than just achieving the final fix. Use the provided rubrics to maintain consistency.
