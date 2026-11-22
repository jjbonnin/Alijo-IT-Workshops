# Instructor Lesson Plan: Workshop 4 — Linux Server Administration
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

---

## 1. Session Overview
* **Target Audience:** Vocational / Secondary & Higher-Ed IT Students, Junior Systems Administrators
* **Duration:** 3 Hours (180 Minutes)
* **Delivery Format:** Hands-on CLI Lab on Ubuntu Server 22.04 / 24.04 LTS
* **Core Theme:** Administering Linux servers safely using least-privilege permissions, `systemd` service controls, `ufw` host firewalling, Bash health automation, and structured log diagnostics.

---

## 2. Minute-by-Minute Pacing Schedule

| Block | Duration | Topic & Lab Module | Key Instructor Actions |
| :--- | :--- | :--- | :--- |
| **1** | `00:00 – 00:30` (30m) | **Server Baseline & CLI Orientation** (`Materials-and-Requirements.md`) | Verify student SSH access, confirm clean VM snapshots exist, and guide completion of `Server-Baseline-Record.md`. |
| **2** | `00:30 – 01:05` (35m) | **Users, Groups & POSIX Permissions** (`Users-Groups-and-Permissions.md`) | Explain `rwx` octal modes (`750` vs `640`), warn against `chmod 777` and `usermod -G` without `-a`, verify `dev_ana` vs `audit_rui` tests. |
| **3** | `01:05 – 01:40` (35m) | **`systemd` Services & `ufw` Firewall** (`Service-Management.md`) | Demonstrate `apache2ctl configtest` before `reload`, emphasize allowing `22/tcp` before `ufw enable` to prevent SSH lockouts. |
| **4** | `01:40 – 02:10` (30m) | **Bash Health Monitoring Script** (`Scripts/server_report.sh`) | Walk through script structure, exit status (`$?`), permissions (`chmod +x`), and custom metric extension in `Bash-Script-Record.md`. |
| **5** | `02:10 – 03:00` (50m) | **Logs, Final Outage Challenge & Debrief** (`Final-Management-Challenge.md`) | Inject or assign the 5-fault production outage scenario, coach students using the 5-layer methodology, and review `Incident-Report.md`. |

---

## 3. Common Student Pitfalls & Coaching Notes
1. **SSH Lockout on `ufw enable`:** Remind students twice to run `sudo ufw allow 22/tcp` *before* enabling `ufw`. Keep console access open in VMware/VirtualBox as a fallback.
2. **Omitting `-a` in `usermod -aG`:** Point out that `usermod -G group user` replaces all supplementary groups rather than appending.
3. **Confusing Directory `x` Bit:** Clarify that without execute (`x`) permission on `/srv/alijo-portal`, `audit_rui` cannot traverse into the directory even if a file inside were readable.
4. **Reaching for `chmod 777` or `ufw disable`:** Enforce the workshop rule that any solution disabling `ufw` or setting `777` fails the security rubric.
