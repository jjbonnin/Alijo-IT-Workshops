# Competency Assessment Rubric: Workshop 4 — Linux Server Administration
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

---

## 1. Grading Overview (100 Points Total)

| Competency Domain | Weight | Evaluation Evidence |
| :--- | :--- | :--- |
| **1. Server Baseline & CLI Navigation** | 15 pts | `Worksheets/Server-Baseline-Record.md` |
| **2. Users, Groups & Least-Privilege Permissions** | 20 pts | `Worksheets/Users-Groups-and-Permissions-Record.md` & live `/srv/alijo-portal` permissions |
| **3. `systemd` Service & `ufw` Firewall Hardening** | 20 pts | `Worksheets/Service-Management-Record.md` & live `systemctl` / `ufw` checks |
| **4. Bash Automation & Health Reporting** | 15 pts | `Worksheets/Bash-Script-Record.md` & working custom enhancement in `server_report.sh` |
| **5. Final Outage Recovery & Post-Mortem Report** | 30 pts | Live recovery of `alijo-srv01` + `Worksheets/Incident-Report.md` |

---

## 2. Detailed Performance Criteria

### Domain 1: Server Baseline & CLI Navigation (15 Points)
* **Exemplary (13–15 pts):** All host identity, CPU/RAM/disk, network interface/gateway, and initial daemon metrics are accurately recorded; clean VM snapshot verified before lab modifications.
* **Proficient (10–12 pts):** Most baseline values recorded accurately with minor omissions in DNS or interface CIDR notation.
* **Developing (0–9 pts):** Incomplete baseline record or missing VM recovery snapshot.

### Domain 2: Users, Groups & Least-Privilege Permissions (20 Points)
* **Exemplary (18–20 pts):** `dev_ana` (`webadmins`) and `audit_rui` (`auditors`) created accurately using `usermod -aG`; `/srv/alijo-portal` set to `750` (`root:webadmins`) and `.env` set to `640`; boundary tests and reflection answers fully accurate.
* **Proficient (14–17 pts):** Users and groups configured properly, with minor permission discrepancy or incomplete reflection explanation.
* **Developing (0–13 pts):** Uses overly permissive modes (`777` or `666`), omits `-a` in `usermod`, or fails access boundary checks.

### Domain 3: `systemd` Service & `ufw` Firewall Hardening (20 Points)
* **Exemplary (18–20 pts):** Both `ssh` and `apache2` active and enabled at boot; `apache2ctl configtest` validated before reload; `ufw` active with `default deny incoming` and explicit rules for `22/tcp` and `80/tcp` only.
* **Proficient (14–17 pts):** Services running and firewall enabled, but missing boot enablement (`systemctl enable`) or config syntax validation step.
* **Developing (0–13 pts):** Disables `ufw` completely or leaves Apache2 broken/unverified.

### Domain 4: Bash Automation & Health Reporting (15 Points)
* **Exemplary (13–15 pts):** `Scripts/server_report.sh` runs cleanly with exit code `0`; student implements a functional custom health check and provides a valid `07:30` `crontab` entry.
* **Proficient (10–12 pts):** Script runs cleanly and worksheet is filled out, but custom health check or `cron` syntax contains minor errors.
* **Developing (0–9 pts):** Script fails to execute or custom check breaks script execution.

### Domain 5: Final Outage Recovery & Post-Mortem Report (30 Points)
* **Exemplary (27–30 pts):** All 5 production faults diagnosed systematically and resolved cleanly (`HTTP 200 OK` on `/status.html`, `.env` hardened to `640`, `ufw` active with `23/tcp` removed and `80/tcp` allowed, `server_report.sh` executable); `Incident-Report.md` documents exact diagnostic commands, root causes, and preventive safeguards.
* **Proficient (21–26 pts):** Restores web connectivity and resolves 4 of 5 faults cleanly, with minor gaps in root-cause documentation.
* **Developing (0–20 pts):** Resolves fewer than 4 faults, disables `ufw`, or applies `chmod 777` workarounds.

---

## 3. Automatic Security Penalties
* **Disabling `ufw` (`ufw disable`) during Final Challenge:** `-10 points`
* **Applying world-writable permissions (`777` / `666`) to web or config files:** `-10 points`
