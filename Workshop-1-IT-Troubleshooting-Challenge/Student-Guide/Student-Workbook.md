# Student Workbook — Workshop 1: IT Troubleshooting Challenge

*Practical Approaches to IT Projects and Problem-Solving* | **Alijó IT Workshops**

---

## 1. Workshop Overview

**Aim:** Resolve computer incidents using a structured methodology of diagnosis, intervention, and verification.

By the end of this workshop, you will be able to:
* Follow a repeatable troubleshooting process instead of guessing.
* Collect relevant information and distinguish symptoms from causes.
* Use basic Linux diagnostic commands in an Ubuntu Desktop virtual machine.
* Apply a controlled fix and verify that the service or application works again.
* Record actions, results, and evidence in a clear technical incident report.
* Work collaboratively and communicate technical findings.

---

## 2. Materials and Preparation

| Area | Materials / Requirements |
| :--- | :--- |
| **Hardware** | One Windows PC per team of 4–5 students; keyboard, mouse, and display. |
| **Virtualisation** | Oracle VM VirtualBox installed and tested. |
| **Virtual machine** | Ubuntu Desktop VM, preferably with a clean snapshot taken before the workshop. |
| **Network** | Working internet or local network connection; network access must be available to the VM. |
| **Student documents** | This workbook, incident cards, diagnostic checklist, incident log, and final report template. |

### Recommended VM Baseline

Before beginning any troubleshooting scenarios, confirm the following baseline setup with your team and instructor:
* The Ubuntu Desktop VM boots successfully and you can log in with the supplied lab account.
* A clean snapshot named `BASELINE – BEFORE WORKSHOP` exists.
* Use only the disposable VM. **Do not** perform disruptive tests on the host computer or the school network.
* Ensure your team knows how to restore the VM between groups or before the surprise incident.
* **Never** change router, DHCP server, or school-network settings.

---

## 3. Three-Hour Schedule

| Duration | Activity | Expected Outcome |
| :--- | :--- | :--- |
| **15 min** | Welcome, challenge briefing, and team roles | Understand the mission, safety rules, and expected deliverables. |
| **20 min** | Troubleshooting methodology | Learn the diagnosis workflow and how to record evidence. |
| **20 min** | Initial inspection and evidence collection | Inspect the VM, establish a baseline, and record system/network information. |
| **60 min** | Incident-solving rounds (3–4 incidents) | Investigate, fix, verify, and document assigned incident cards. |
| **25 min** | Surprise incident | Apply the same method to an unfamiliar fault under time pressure. |
| **20 min** | Verification and technical documentation | Re-test the system and complete the incident report. |
| **20 min** | Team presentations and evaluation | Present findings, explain evidence, and reflect on the process. |

> **Total: 180 minutes.** The schedule includes short transitions within each block; keep the incident-solving phase focused so your team has time to complete its report.

---

## 4. Team Organisation

| Role | Main Responsibilities |
| :--- | :--- |
| **Team coordinator** | Keeps the team on task, reads the incident brief, and makes sure decisions are agreed upon. |
| **Lead technician** | Runs diagnostic commands and performs approved changes. |
| **Evidence recorder** | Writes down symptoms, commands, outputs, and timestamps. |
| **Verifier / tester** | Defines and performs the tests that prove the fix worked. |
| **Reporter** *(for teams of five)* | Prepares the final explanation and presents the results. |

* **Teams of four:** Combine the **Reporter** and **Team coordinator** roles.
* **Role rotation:** Rotate the **Lead technician** role between incidents so that everyone participates directly on the command line.

---

## 5. Troubleshooting Methodology

Follow these seven steps strictly in order for every incident:

| Step | Action | Questions to Ask |
| :--- | :--- | :--- |
| **1. Identify** | Understand the problem. | What is not working? Who is affected? When did it start? |
| **2. Gather evidence** | Observe and collect facts before changing anything. | What do error messages, status outputs, and logs show? |
| **3. Form a hypothesis** | Identify the most likely cause. | Which evidence supports this explanation? |
| **4. Test the hypothesis** | Run a low-risk test. | What result would confirm or reject the hypothesis? |
| **5. Implement a fix** | Make one controlled change at a time. | Can the change be reversed? Is it within the lab scope? |
| **6. Verify** | Repeat the original test and perform a related test. | Does the original function work? Did anything else break? |
| **7. Document** | Record the cause, fix, and evidence. | Could another technician understand and reproduce the work? |

### Diagnostic Command Quick Reference (Ubuntu)

| Purpose | Command |
| :--- | :--- |
| Current user and machine | `whoami ; hostname` |
| IP addresses and interfaces | `ip address` |
| Routing table / default gateway | `ip route` |
| Test reachability | `ping -c 4 1.1.1.1` |
| Test DNS resolution | `getent hosts example.com` |
| Show DNS configuration | `resolvectl status` |
| Check a service | `systemctl status SERVICE_NAME` |
| Check listening ports | `ss -tulpn` |
| Check disk space | `df -h` |
| Check directory permissions | `ls -ld PATH` |
| Inspect recent system logs | `journalctl -n 30 --no-pager` |
| Check application process | `ps aux` |

> **Command Usage Rule:** Use only commands relevant to the incident. Some commands may require administrator privileges—always ask your teacher before using `sudo` for a system change.
