# Slide Deck Outline: Workshop 4 — Linux Server Administration
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

---

## Slide 1: Title Slide
* **Title:** Workshop 4: Linux Server Administration
* **Subtitle:** Practical Approaches to IT Projects and Problem-Solving — Alijó IT Workshops
* **Visual:** Terminal prompt (`sysadmin@alijo-srv01:~$`) alongside Ubuntu Server, `systemd`, and `ufw` architecture icons.

## Slide 2: Learning Outcomes & Lab Safety Rules
* **Key Outcomes:**
  * Baseline and monitor Linux server health from the CLI.
  * Implement role-based access control using POSIX permissions (`750`, `640`, `644`).
  * Manage background daemons with `systemd` and harden ports with `ufw`.
  * Automate health checks in Bash and diagnose multi-layer outages.
* **Non-Negotiable Rules:** Never log in directly as `root`, never use `chmod 777`, never disable `ufw` to fix connectivity.

## Slide 3: Module 1 — Server Baseline & Filesystem Hierarchy
* **Key Directories:** `/etc` (configs), `/var/log` (logs), `/var/www/html` (public web root), `/srv` (site-specific application data), `/usr/local/bin` (custom admin scripts).
* **Core Inspection Commands:** `hostnamectl`, `ip -br -4 addr`, `df -h`, `free -h`, `ss -tulpn`.

## Slide 4: Module 2 — Users, Groups & POSIX Permissions
* **Permission Bits:** Read (`r=4`), Write (`w=2`), Execute (`x=1`) across Owner (`u`), Group (`g`), and Others (`o`).
* **Critical Distinction:** Execute (`x`) on a directory means *traversal* (`cd`), not running it as a script.
* **Best Practices:** Always append groups with `usermod -aG`; protect secrets with `640` (`rw-r-----`).

## Slide 5: Module 3 — `systemd` Service Lifecycle
* **Runtime vs. Boot State:** `start/stop` vs. `enable/disable` (or combined `systemctl enable --now <service>`).
* **Zero-Downtime Config Updates:** Always run `sudo apache2ctl configtest` (`Syntax OK`) before `sudo systemctl reload apache2`.

## Slide 6: Module 4 — Host Firewall Hardening (`ufw`)
* **Default Posture:** `default deny incoming`, `default allow outgoing`.
* **Anti-Lockout Rule:** Always `sudo ufw allow 22/tcp` **before** running `sudo ufw enable`.
* **Auditing Rules:** `sudo ufw status numbered` and `sudo ss -tulpn`.

## Slide 7: Module 5 — Bash Automation (`server_report.sh`)
* **Anatomy of an Ops Script:** Shebang (`#!/usr/bin/env bash`), strict error flags (`set -u`), formatted sections, and exit codes (`echo $?`).
* **Scheduling:** Automating daily reports via `cron` (`30 7 * * *`).

## Slide 8: Module 6 — 5-Layer Troubleshooting Methodology
* **Bottom-Up Diagnostic Stack:**
  1. **Host Resources:** `df -h`, `free -h`
  2. **Service & Logs:** `systemctl status`, `journalctl -xe`, `/var/log/apache2/error.log`
  3. **Listening Sockets:** `ss -tulpn`
  4. **Network & Firewall:** `ip addr`, `ufw status verbose`
  5. **File Ownership & Permissions:** `ls -la`, `namei -l`

## Slide 9: Final Management Challenge Briefing (`INC-401`)
* **Scenario:** Post-maintenance outage on `alijo-srv01` affecting `/status.html`, `.env` permissions, `ufw` rules, and `server_report.sh`.
* **Deliverables:** Live server restoration (`HTTP 200 OK`) + completed `Worksheets/Incident-Report.md`.
