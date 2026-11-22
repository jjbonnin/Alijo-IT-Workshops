# Workshop 4: Linux Server Administration
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

---

## 1. Workshop Overview
In this hands-on workshop, you will step into the role of a Junior Linux Systems Administrator responsible for provisioning, securing, automating, and troubleshooting an **Ubuntu Server LTS** production node. Moving beyond basic desktop navigation, you will manage system users and POSIX file permissions, administer `systemd` services and `ufw` firewall rules, write a reusable Bash health-monitoring script, and diagnose live service outages using system logs.

---

## 2. Learning Objectives
By the end of this workshop, you will be able to:
1. Inspect hardware, storage, memory, network interfaces, and kernel baseline metrics using standard Linux CLI utilities.
2. Create administrative and service user accounts, configure group memberships, and enforce least-privilege file/directory permissions (`chmod`, `chown`).
3. Manage background daemons with `systemd` (`systemctl`), validate configuration syntax prior to restarts, and apply targeted host firewall rules (`ufw`).
4. Automate recurring server health checks in a clean, executable Bash script (`Scripts/server_report.sh`).
5. Investigate and resolve broken services and permission/firewall incidents using `journalctl`, `/var/log/*`, and `ss`.

---

## 3. Repository Structure

```text
Workshop-4-Linux-Server-Administration/
├── README.md
├── Scripts/
│   └── server_report.sh
├── Student-Guide/
│   ├── Materials-and-Requirements.md
│   ├── Linux-Command-Reference.md
│   ├── Users-Groups-and-Permissions.md
│   ├── Service-Management.md
│   ├── Logs-and-Troubleshooting.md
│   └── Final-Management-Challenge.md
└── Worksheets/
    ├── Server-Baseline-Record.md
    ├── Users-Groups-and-Permissions-Record.md
    ├── Service-Management-Record.md
    ├── Bash-Script-Record.md
    └── Incident-Report.md
```

---

## 4. Recommended Execution Sequence
1. **Preparation & Baseline (`30 min`):** Review `Student-Guide/Materials-and-Requirements.md` and `Student-Guide/Linux-Command-Reference.md`, verify your Ubuntu Server snapshot, and complete `Worksheets/Server-Baseline-Record.md`.
2. **Identity & Permissions (`35 min`):** Follow `Student-Guide/Users-Groups-and-Permissions.md` and record outcomes in `Worksheets/Users-Groups-and-Permissions-Record.md`.
3. **Services & Host Firewall (`35 min`):** Follow `Student-Guide/Service-Management.md` and document service/firewall states in `Worksheets/Service-Management-Record.md`.
4. **Bash Monitoring Automation (`30 min`):** Inspect, extend, and run `Scripts/server_report.sh`, documenting your implementation in `Worksheets/Bash-Script-Record.md`.
5. **Logs, Troubleshooting & Final Challenge (`50 min`):** Complete `Student-Guide/Logs-and-Troubleshooting.md` and `Student-Guide/Final-Management-Challenge.md`, submitting `Worksheets/Incident-Report.md`.
