---
marp: true
theme: default
paginate: true
backgroundColor: #0f172a
color: #f8fafc
header: "Alijó IT Workshops | Workshop 4: Linux Server Administration"
footer: "Practical Approaches to IT Projects and Problem-Solving"
style: |
  section::before {
    content: "";
    position: absolute;
    top: 22px;
    right: 28px;
    width: 110px;
    height: 75px;
    background-image: url('../../00-Shared-Resources/Assets/logo-ies-sa-colomina-dark.jpg');
    background-size: contain;
    background-repeat: no-repeat;
    opacity: 0.85;
    pointer-events: none;
  }
---

![bg opacity:0.35](../../Workshop-1-IT-Troubleshooting-Challenge/Assets/slides/cover-w1.jpg)

## 0. Workshop 4: Linux Server Administration

### Practical Approaches to IT Projects and Problem-Solving

**Agrupamento de Escolas D. Sancho II, Alijó**

*Ponente: Juan José Bonnín Sansó (IES Sa Colomina)*

---

# Workshop 4: Linux Server Administration
### Practical Approaches to IT Projects and Problem-Solving
**Alijó IT Workshops**

* **Duration:** 180 Minutes (3 Hours)
* **Format:** Hands-On Server Ops Lab (Teams of 4–5 students)
* **Environment:** Ubuntu Server LTS (`alijo-srv01`) via SSH / Console

> **Visual / Imagen recomendada (Portada):**
> *Ilustración minimalista sobre fondo azul oscuro mostrando el prompt `sysadmin@alijo-srv01:~$` junto a iconos de servidor Ubuntu, escudo de firewall `ufw` y engranajes de `systemd`.*
> *Prompt IA sugerido:* `"Minimalist dark-blue tech presentation cover illustration, Ubuntu Linux server rack connected to a glowing cyan firewall shield and terminal prompt window, clean flat vector style, no text"`

<!--
Notas del orador (00–05 min):
- Presenta el salto de este taller: pasamos de un entorno de escritorio a administrar un servidor Linux en producción (`alijo-srv01`) exclusivamente desde la línea de comandos.
-->

---

## 1. Mission & Learning Outcomes

By the end of this 3-hour workshop, your team will be able to:

1. **Inspect server baseline metrics** (CPU, RAM, disk, network, listening sockets) from the CLI.
2. **Provision users and groups** safely (`usermod -aG`) and enforce least-privilege POSIX permissions (`750`, `640`, `644`).
3. **Administer `systemd` daemons** (`apache2`, `ssh`) with syntax validation before reload.
4. **Harden host network access** with `ufw` (`default deny incoming`) without locking out SSH.
5. **Automate health checks** in Bash (`server_report.sh` + `cron`) and resolve multi-layer outages (`INC-401`).

> **Visual / Imagen recomendada:**
> *Diagrama de 4 pilares: `[1. Identidad y Permisos]` • `[2. Servicios systemd]` • `[3. Firewall ufw]` • `[4. Bash/Cron + Diagnóstico]`.*

<!--
Notas del orador (05–10 min):
- Recalca que en producción cada cambio de configuración se valida antes de recargar el servicio para evitar caídas innecesarias.
-->

---

## 2. Three-Hour Session Roadmap (180 Min)

| Block | Duration | Activity | Team Deliverable |
| :--- | :--- | :--- | :--- |
| **1** | 30 min | Briefing, safety rules & server baseline inspection | `Server-Baseline-Record.md` |
| **2** | 35 min | Users, groups (`webadmins`, `auditors`) & POSIX permissions | `Users-Groups-and-Permissions-Record.md` |
| **3** | 35 min | `systemd` lifecycle & `ufw` host firewall hardening | `Service-Management-Record.md` |
| **4** | 30 min | Bash health script (`server_report.sh`) & `cron` scheduling | `Bash-Script-Record.md` |
| **5** | 15 min | *Break + Instructor fault injection (`INC-401`)* | — |
| **6** | 35 min | **Final Management Challenge (`INC-401`)** & debrief | `HTTP 200 OK` + `Incident-Report.md` |

> **Visual / Imagen recomendada:**
> *Línea de tiempo horizontal en 6 bloques destacando la inyección de fallos en el descanso y el reto final `INC-401`.*

<!--
Notas del orador (10–12 min):
- Confirma que todos tienen creado el snapshot limpio `BASELINE - CLEAN UBUNTU SERVER` antes de empezar.
-->

---

## 3. Non-Negotiable Server Ops Safety Rules

1. **Never Log In Directly as `root`:** Work as `sysadmin` and elevate privilege explicitly with `sudo`.
2. **Never Use `chmod 777` (or `666`):** World-writable files or `.env` secrets incur automatic rubric penalties (`-10 pts`).
3. **Never Run `ufw disable` to Troubleshoot:** Open only required ports (`22/tcp`, `80/tcp`) while keeping default-deny active (`-10 pts` penalty if disabled).
4. **Anti-Lockout Order:** Always run `sudo ufw allow 22/tcp` **before** enabling `ufw`.
5. **Validate Before Reload:** Run `sudo apache2ctl configtest` (`Syntax OK`) before `sudo systemctl reload apache2`.

> **Visual / Imagen recomendada:**
> *Tarjeta visual de advertencia en rojo/ámbar con las 3 prohibiciones críticas: `NO root login`, `NO chmod 777`, `NO ufw disable`.*

<!--
Notas del orador (12–15 min):
- Deja muy claro desde el minuto 1 que usar `chmod 777` o `ufw disable` invalida la solución aunque la página web cargue.
-->

---

## 4. Module 1: Server Baseline & Filesystem Hierarchy

Know where critical server files live and how to inspect system health:

| Directory | Purpose | Key Inspection Commands |
| :--- | :--- | :--- |
| `/etc/` | System & service configuration files (`ssh`, `apache2`, `ufw`) | `hostnamectl`, `cat /etc/os-release` |
| `/var/log/` | System journals, auth logs, Apache access/error logs | `journalctl -xe`, `tail -n 30 /var/log/apache2/error.log` |
| `/var/www/html/` | Default public Apache web root (`status.html`) | `ls -la /var/www/html/` |
| `/srv/` | Site-specific application data (`/srv/alijo-portal`) | `ls -la /srv/alijo-portal/` |
| **Network & Load** | Interfaces, routes, RAM, disk, and open sockets | `ip -br -4 addr`, `free -h`, `df -h`, `sudo ss -tulpn` |

> **Visual / Imagen recomendada:**
> *Captura real de terminal en `alijo-srv01` mostrando `ip -br -4 addr`, `df -h /` y `sudo ss -tulpn`.*

<!--
Notas del orador (15–30 min):
- Guía a los equipos mientras completan `Worksheets/Server-Baseline-Record.md` con los valores iniciales de su VM.
-->

---

## 5. Module 2: Users, Groups & Least-Privilege Permissions

### Safe Group Membership
```bash
sudo groupadd -f webadmins
sudo groupadd -f auditors
sudo usermod -aG webadmins dev_ana     # ALWAYS use -aG (append), never -G alone!
sudo usermod -aG auditors audit_rui
```

### Target Permission Matrix (`/srv/alijo-portal`)
| Path | Owner:Group | Mode | Symbolic | Why |
| :--- | :--- | :--- | :--- | :--- |
| `/srv/alijo-portal` | `root:webadmins` | `750` | `drwxr-x---` | `x` allows traversal (`cd`) for `root` & `webadmins` only |
| `/srv/alijo-portal/index.html` | `root:webadmins` | `644` | `-rw-r--r--` | Publicly readable web asset, writable only by `root` |
| `/srv/alijo-portal/.env` | `root:webadmins` | `640` | `-rw-r-----` | Secrets readable by `webadmins`, zero access for `other` |

> **Visual / Imagen recomendada:**
> *Diagrama visual desglosando `640` (`rw- r-- ---`) en bloques de color para `User (root)`, `Group (webadmins)` y `Others`.*

<!--
Notas del orador (30–65 min):
- Explica por qué el bit `x` en un directorio significa permiso de paso (`cd`), mientras que `r` permite listar nombres (`ls`).
-->

---

## 6. Module 3: `systemd` Service Lifecycle

Manage background daemons cleanly without dropping active user sessions:

```bash
# 1. Inspect current state & boot enablement
systemctl status apache2
systemctl is-enabled apache2

# 2. Start now AND enable automatically at boot
sudo systemctl enable --now apache2

# 3. Validate syntax BEFORE applying config changes
sudo apache2ctl configtest          # Must return: Syntax OK
sudo systemctl reload apache2       # Graceful reload (zero dropped connections)
```

* **`reload` vs. `restart`:** `reload` re-reads configuration gracefully; `restart` kills all worker processes and drops active HTTP connections.

> **Visual / Imagen recomendada:**
> *Captura de terminal mostrando `Syntax OK` tras `apache2ctl configtest` seguido de `systemctl status apache2` en verde (`active (running)`).*

<!--
Notas del orador (65–85 min):
- Haz énfasis en la diferencia práctica entre `reload` y `restart`, ya que es una pregunta directa en su hoja de trabajo.
-->

---

## 7. Module 4: Host Firewall Hardening (`ufw`)

Enforce a **default-deny incoming** posture while preserving SSH and HTTP access:

```bash
# 1. Set baseline policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 2. Allow SSH FIRST (anti-lockout!), then HTTP
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp

# 3. Enable and audit numbered rules
sudo ufw --force enable
sudo ufw status numbered
```

> **Visual / Imagen recomendada:**
> *Captura real de `sudo ufw status verbose` mostrando `Default: deny (incoming), allow (outgoing)` y únicamente `22/tcp` y `80/tcp` permitidos.*

<!--
Notas del orador (85–100 min):
- Revisa visualmente en las mesas que `22/tcp` está permitido y que no queda ningún puerto innecesario abierto.
-->

---

## 8. Module 5: Bash Automation & `cron` (`server_report.sh`)

Automate daily server health reporting with strict error handling and exit codes:

```bash
#!/usr/bin/env bash
set -u

echo "=== Alijo Server Health Report ($(date -Iseconds)) ==="
echo "Host: $(hostname) | Uptime: $(uptime -p)"
df -h /
free -h
systemctl is-active apache2 ssh
```

### Execution & Daily `07:30` Schedule (`crontab -e`)
```bash
chmod 750 Scripts/server_report.sh
./Scripts/server_report.sh && echo "Exit code: $?"

# Crontab entry (runs every day at 07:30):
30 7 * * * /home/sysadmin/Alijo-IT-Workshops/Workshop-4-Linux-Server-Administration/Scripts/server_report.sh >> /var/log/server_health.log 2>&1
```

> **Visual / Imagen recomendada:**
> *Diagrama explicando los 5 campos de cron (`30 7 * * *`) + redirección `>> /var/log/server_health.log 2>&1`.*

<!--
Notas del orador (100–130 min):
- Pide a los equipos que añadan una comprobación personalizada (por ejemplo, carga de CPU o estado de `ufw`) y verifiquen que `echo $?` devuelve `0`.
-->

---

![bg right:42% contain](../../Workshop-4-Linux-Server-Administration/Assets/slides/diagram-5-layers.jpg)

## 9. Module 6: 5-Layer Troubleshooting Stack

When an outage hits `alijo-srv01`, diagnose systematically from bottom to top:

```text
[Layer 5: File Ownership & Permissions] ──▶ ls -la /var/www/html /srv/alijo-portal
[Layer 4: Host Firewall (`ufw`)]        ──▶ sudo ufw status numbered
[Layer 3: Listening Sockets]            ──▶ sudo ss -tulpn
[Layer 2: Daemon & Logs (`systemd`)]    ──▶ systemctl status apache2 | journalctl -xe
[Layer 1: Host Resources]               ──▶ df -h | free -h
```

* **Diagnostic Clue:**
  * `Connection refused` on `:80` ➔ Service stopped (Layer 2/3).
  * `Connection timed out` on `:80` ➔ Firewall dropping packets (Layer 4).
  * `HTTP/1.1 403 Forbidden` ➔ File ownership or `600` permissions blocking `www-data` (Layer 5).

> **Visual / Imagen recomendada:**
> *Escalera visual de 5 niveles con el síntoma HTTP asociado a cada capa (`Connection refused`, `Timeout`, `403 Forbidden`).*

<!--
Notas del orador (130–145 min):
- Proyecta esta diapositiva justo antes de iniciar el Reto Final `INC-401` como mapa de diagnóstico.
-->

---

## 10. Final Management Challenge Briefing (`INC-401`)

### Incident Scenario
Following scheduled maintenance on `alijo-srv01`, monitoring reports a multi-layer outage:
* `http://<SERVER_IP>/status.html` is unreachable externally.
* Security audit flags drifted permissions on `/srv/alijo-portal/.env` and legacy firewall rules.
* The daily monitoring script `Scripts/server_report.sh` fails to execute.

### Acceptance Criteria & Grading (100 Points)
1. `curl -i http://<SERVER_IP>/status.html` returns **`HTTP/1.1 200 OK`** (`Alijo Status: Operational`).
2. `/srv/alijo-portal/.env` hardened to **`640` (`root:webadmins`)**; `/var/www/html/status.html` set to **`644` (`root:www-data`)**.
3. `ufw` active with **`23/tcp` removed** and **`80/tcp` allowed**.
4. `Scripts/server_report.sh` executable (`750`) and `Worksheets/Incident-Report.md` completed with before/after evidence.

<!--
Notas del orador (145–180 min):
- Al finalizar y recoger los informes, recuerda a todos restaurar el snapshot `BASELINE - CLEAN UBUNTU SERVER`.
-->

---

![bg right:32% fit](../../00-Shared-Resources/Assets/speaker-jbonnin.jpg.JPG)

## About the Speaker | Juan José Bonnín Sansó

**IT & Vocational Education Teacher (SMX / ASIX) — IES Sa Colomina (Eivissa)**

* **Engineering & Teaching Background:** Engineer and Computer Science / ICT educator since 2015, specialising in Network Services (*Serveis en Xarxa*), Operating Systems, Markup Languages, and Database Administration.
* **E-Learning & Digital Coordination:** Master's in Education & ICT (UOC), former ICT Coordinator, Google Workspace for Education trainer, and co-founder of *TIC Natur – Solucions Formatives*.
* **Beyond the Classroom:** Regional basketball referee (CBAB) since 1985, National Volleyball Referee (**NIII-C**), and licensed coastal skipper.

### Contact & Links
* **Email:** [jjbonninsanso@educaib.eu](mailto:jjbonninsanso@educaib.eu)
* **Web Profile:** [https://about.me/jbonnins](https://about.me/jbonnins)
* **Host Institution:** Agrupamento de Escolas D. Sancho II, Alijó (Portugal)

<!--
Notas del orador (Cierre):
- Agradece la acogida al Agrupamento de Escolas D. Sancho II (Alijó) y deja proyectados tus datos de contacto y el perfil about.me/jbonnins para futuras colaboraciones.
-->
