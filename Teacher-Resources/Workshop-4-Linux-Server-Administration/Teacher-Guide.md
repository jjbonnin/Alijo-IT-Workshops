# Teacher Guide — Workshop 4: Linux Server Administration
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

---

## 1. Session Overview & Pacing (180 Minutes)

| Time | Phase | Instructor Actions | Student Deliverable |
| :--- | :--- | :--- | :--- |
| **00–15 min** | **Briefing & Baseline** | Review CLI safety rules (`sudo`, no `chmod 777`, no `ufw disable`). Verify all teams have the `BASELINE - CLEAN UBUNTU SERVER` snapshot ready. | `Worksheets/Server-Baseline-Record.md` |
| **15–45 min** | **Users, Groups & Permissions** | Demonstrate `usermod -aG` vs. `usermod -G` and octal modes (`750`, `644`, `640`). Audit `/srv/alijo-portal` permissions across teams. | `Worksheets/Users-Groups-and-Permissions-Record.md` |
| **45–75 min** | **`systemd` & `ufw` Hardening** | Emphasize running `apache2ctl configtest` before `reload` and allowing `22/tcp` before `ufw enable`. | `Worksheets/Service-Management-Record.md` |
| **75–105 min** | **Bash Automation & `cron`** | Guide teams through `Scripts/server_report.sh`, exit codes (`$?`), and scheduling the `07:30` `crontab` job. | `Worksheets/Bash-Script-Record.md` |
| **105–120 min** | **Break & Fault Injection** | Run the 5-fault injection script (`Solutions-and-Setup/Service-and-Incident-Setup.md`) on student VMs while teams take a break. | — |
| **120–165 min** | **Final Management Challenge (`INC-401`)** | Coach teams to use the 5-layer bottom-up diagnostic stack without jumping straight to `ufw disable` or `777`. | Live `HTTP 200 OK` + `Worksheets/Incident-Report.md` |
| **165–180 min** | **Debrief & Snapshot Reset** | Review the 5 root causes, collect incident reports, and restore VMs to `BASELINE - CLEAN UBUNTU SERVER`. | — |

---

## 2. Critical Safety & Facilitation Checkpoints
* **SSH Anti-Lockout:** Before any student runs `sudo ufw enable`, visually confirm that `22/tcp` is already added (`sudo ufw status`).
* **Zero-Tolerance Shortcuts:** Immediately flag any use of `chmod 777` or `ufw disable` during troubleshooting, as both trigger automatic rubric penalties.
* **Reference Files:**
  * [Instructor Setup Guide](./Instructor-Setup-Guide.md)
  * [Answer Key](./Answer-Key.md)
  * [Assessment Rubric](./Assessment-Rubric.md)
  * [Presentation Outline](./Presentation-Outline.md)
