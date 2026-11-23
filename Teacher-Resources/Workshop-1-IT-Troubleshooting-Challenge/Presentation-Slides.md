---
marp: true
theme: default
paginate: true
backgroundColor: #0f172a
color: #f8fafc
header: "Alijó IT Workshops | Workshop 1: IT Troubleshooting Challenge"
footer: "Practical Approaches to IT Projects and Problem-Solving"
style: |
  section::after {
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
  }
---

![bg opacity:0.35](../../Workshop-1-IT-Troubleshooting-Challenge/Assets/slides/cover-w1.jpg)

# Workshop 1: IT Troubleshooting Challenge
### Practical Approaches to IT Projects and Problem-Solving
**Agrupamento de Escolas D. Sancho II, Alijó**

*Ponente: Juan José Bonnín Sansó (IES Sa Colomina)*

---

![bg opacity:0.35](../../Workshop-1-IT-Troubleshooting-Challenge/Assets/slides/cover-w1.jpg)
# Workshop 1: IT Troubleshooting Challenge
### Practical Approaches to IT Projects and Problem-Solving
**Alijó IT Workshops**

* **Duration:** 180 Minutes (3 Hours)
* **Format:** Team-based Hands-On Lab (4–5 students per team)
* **Environment:** Ubuntu Desktop VM (Oracle VM VirtualBox)

> **Visual / Imagen recomendada (Portada):**
> *Captura limpia de terminal Ubuntu junto a una tarjeta de incidente técnico (`INC-01`) o ilustración minimalista en tonos azul oscuro/cian de un ingeniero diagnosticando una red.*
> *Prompt IA sugerido:* `"Minimalist dark-blue tech presentation cover illustration, Ubuntu Linux terminal window with green diagnostic checkmarks and network topology nodes, clean flat vector style, no text"`

<!--
Notas del orador (00–05 min):
- Da la bienvenida al equipo y presenta el objetivo central: dejar de adivinar ("probar comandos al azar") y trabajar como un equipo real de soporte nivel 2.
- Confirma que todos tienen VirtualBox abierto y la VM lista.
-->

---

## 1. Mission & Learning Outcomes

By the end of this 3-hour challenge, your team will be able to:

1. **Follow a repeatable 7-step methodology** instead of guessing.
2. **Distinguish symptoms from root causes** using verifiable CLI evidence.
3. **Diagnose Linux system, network, DNS, and service faults** safely.
4. **Apply controlled, reversible fixes** without breaking unrelated services.
5. **Document findings and proof** in a professional Technical Incident Report.

> **Visual / Imagen recomendada:**
> *Iconos de flujo en 3 bloques: `[Síntoma Observado]` ➔ `[Evidencia CLI]` ➔ `[Causa Raíz + Verificación]`.*

<!--
Notas del orador (05–10 min):
- Recalca que "ya funciona" no es una respuesta válida sin evidencia (salida de comando o captura antes/después).
-->

---

## 2. Three-Hour Session Roadmap (180 Min)

| Block | Duration | Activity | Team Deliverable |
| :--- | :--- | :--- | :--- |
| **1** | 15 min | Briefing, safety rules & team role assignment | Roles assigned |
| **2** | 20 min | 7-Step Troubleshooting Methodology | Method review |
| **3** | 20 min | VM Baseline Inspection & Snapshot verification | `Baseline-Record` |
| **4** | 60 min | **Incident-Solving Rounds (3–4 Incident Cards)** | Incident Logs |
| **5** | 25 min | **Surprise Incident** (timed live fault) | Live recovery |
| **6** | 20 min | Final verification & Incident Report completion | `Final-Report.md` |
| **7** | 20 min | Team presentations & debrief | 3-min pitch |

> **Visual / Imagen recomendada:**
> *Línea de tiempo horizontal dividida en 7 bloques de color destacando los 60 min de rondas y los 25 min del incidente sorpresa.*

<!--
Notas del orador (10–12 min):
- Avisa de que los tiempos son estrictos y que deben reservar siempre los últimos 20 minutos para cerrar el informe técnico antes de exponer.
-->

---

## 3. Team Roles & Rotation Rules

Every team (4–5 members) operates with clear operational roles:

* **Team Coordinator:** Keeps time, reads the incident card, validates team consensus before any change. *(In teams of 4, combines with Reporter)*.
* **Lead Technician:** Executes diagnostic commands and approved fixes on the terminal.
* **Evidence Recorder:** Captures symptoms, exact commands, outputs, and timestamps.
* **Verifier / Tester:** Defines and runs the acceptance test proving recovery.
* **Reporter:** Synthesizes findings and presents the post-mortem.

> **Mandatory Rule:** Rotate the **Lead Technician** role after every incident so every student drives the CLI.

> **Visual / Imagen recomendada:**
> *Diagrama circular con 5 roles conectados y flechas de rotación entre rondas.*

<!--
Notas del orador (12–15 min):
- Pide que cada equipo elija ahora mismo quién empieza como Lead Technician y quién registra evidencias.
-->

---

## 4. Non-Negotiable Lab Safety Rules

Before touching any configuration file, verify these **5 golden rules**:

1. **Snapshot First:** Confirm `BASELINE – BEFORE WORKSHOP` exists in VirtualBox before starting.
2. **VM Only:** Run diagnostics exclusively inside the disposable Ubuntu VM — never on the host PC.
3. **Never Touch Campus Network:** Do not modify host Wi-Fi/Ethernet, router, or school DHCP settings.
4. **One Change at a Time:** Never apply multiple edits simultaneously; test after each action.
5. **No Destructive Shortcuts:** Never use `chmod 777`, `rm -rf` on system paths, or disable firewalls to mask a problem.

> **Visual / Imagen recomendada:**
> *Captura real de Oracle VM VirtualBox mostrando la ventana de Snapshots con `BASELINE – BEFORE WORKSHOP` seleccionado.*

<!--
Notas del orador (15–20 min):
- Pide a todos los equipos que te muestren en pantalla el snapshot `BASELINE – BEFORE WORKSHOP` antes de pasar a la metodología.
-->

---

## 5. The 7-Step Troubleshooting Methodology

Follow these steps **strictly in order** for every incident card:

```text
[1. Identify & Reproduce] ──▶ [2. Gather Baseline Info] ──▶ [3. Form Hypotheses]
                                                                     │
[7. Document & Close] ◀── [6. Verify & Regression Test] ◀── [4. Test & Isolate]
                                                                     │
                                                           [5. Controlled Fix]
```

* **Golden Principle:** Never jump from Step 1 (Symptom) directly to Step 5 (Fix).
* If Step 6 fails, **revert your change** and return to Step 3 with new evidence.

> **Visual / Imagen recomendada:**
> *Diagrama vectorial limpio de 7 pasos numerados en bucle cerrado (puedes exportar el esquema ASCII superior como SVG con fondo oscuro).*

<!--
Notas del orador (20–30 min):
- Pon un ejemplo rápido: "Si una web no carga, reiniciar el servidor a ciegas no diagnostica si el fallo era DNS, firewall o el proceso caído".
-->

---

## 6. Step 2 & 4 Toolkit: Essential Linux Diagnostics

Use targeted commands by layer instead of random trial-and-error:

| Layer | Diagnostic Commands | What It Proves |
| :--- | :--- | :--- |
| **System & Resources** | `uptime`, `df -h`, `free -h`, `ps aux` | Disk full, RAM exhaustion, hung processes |
| **Services & Logs** | `systemctl status <svc>`, `journalctl -xe` | Crashed daemons, config syntax errors |
| **Network Link & IP** | `ip -br a`, `ip route`, `ping -c 3 <GW>` | Interface down, wrong IP/subnet, missing gateway |
| **DNS & Ports** | `resolvectl status`, `dig`, `ss -tulpn`, `curl -I` | Broken name resolution, closed listening port |
| **Permissions & Files** | `ls -la <path>`, `id`, `namei -l <path>` | Ownership mismatch, missing `r`/`x` bits |

> **Visual / Imagen recomendada:**
> *Captura real de terminal Ubuntu mostrando la salida coloreada de `ip -br a` y `ss -tulpn`.*

<!--
Notas del orador (30–35 min):
- Deja esta diapositiva proyectada o impresa como referencia rápida durante la fase de inspección inicial.
-->

---

## 7. Phase 3: Initial VM Baseline Inspection (20 Min)

Before any faults are injected, inspect your healthy VM and record:

1. **OS & Kernel:** `hostnamectl`
2. **Network Interface & IPv4:** `ip -br -4 addr` and `ip route`
3. **DNS Resolver:** `resolvectl status` (or `/etc/resolv.conf`)
4. **Disk & Memory:** `df -h /` and `free -h`
5. **Active Services & Ports:** `ss -tulpn`

> **Checkpoint:** You cannot spot what changed during an outage if you never measured what "healthy" looked like.

> **Visual / Imagen recomendada:**
> *Captura de `Worksheets/Baseline-Record.md` parcialmente rellenado como ejemplo.*

<!--
Notas del orador (35–55 min):
- Recorre las mesas comprobando que los equipos anotan la IP de su VM, la puerta de enlace y el servidor DNS activo.
-->

---

## 8. Phase 4 & 5: Incident Rounds & Surprise Challenge

### Round 1 — Assigned Incident Cards (60 Min)
* Solve **3–4 structured incidents** (network, DNS, permissions, background service/script).
* Log every command and output in your `Incident-Log.md` **before** applying any fix.
* Call the instructor for a quick checkpoint verification after each resolved card.

### Round 2 — Surprise Incident (25 Min)
* Restored baseline + **unannounced live fault** injected by the instructor.
* Full 7-step methodology under realistic time pressure.

> **Visual / Imagen recomendada:**
> *Mockup de una tarjeta de incidente (`INC-03: Internal Application Unreachable`) con campos de Síntoma, Impacto y Restricciones.*

<!--
Notas del orador (55–140 min):
- Entrega las tarjetas de incidentes progresivamente; si un equipo se atasca más de 12 minutos en una pista, haz una pregunta guía ("¿Qué dice la capa inferior?") en lugar de dar el comando.
-->

---

## 9. Evidence Standards & Final Report (`Final-Report.md`)

A professional incident report requires **verifiable proof**, not summaries:

* **Weak (0 pts):** *"We fixed the network and now it works."*
* **Strong (Full pts):**
  * **Before:** `ping -c 2 intranet.alijo.local` → `Temporary failure in name resolution`
  * **Root Cause:** `/etc/resolv.conf` pointed to an unreachable nameserver (`192.0.2.99`).
  * **Fix:** Restored valid DNS resolver and verified `dig intranet.alijo.local +short` → `192.168.10.10`.
  * **After:** `curl -I http://intranet.alijo.local:8080` → `HTTP/1.1 200 OK`.

> **Visual / Imagen recomendada:**
> *Comparativa visual lado a lado: tarjeta roja ("Informe sin evidencia") vs. tarjeta verde ("Informe con salida CLI antes/después").*

<!--
Notas del orador (140–160 min):
- Recuerda a los equipos que peguen las salidas reales de terminal en las secciones 4, 7 y 8 de `Final-Report.md`.
-->

---

## 10. Final Presentations & Evaluation Criteria (20 Min)

Each team delivers a **3-minute technical briefing** covering:

1. **Incident Overview:** Symptoms & business impact.
2. **Diagnostic Trail:** Key commands that isolated the root cause (and dead ends ruled out).
3. **Fix & Verification:** Exact change applied and proof of recovery.
4. **Prevention:** One concrete safeguard to prevent recurrence.

### Grading Weights (100 Points)
* **Methodology & Safety Discipline:** 30 pts
* **Diagnostic Accuracy & Root Cause:** 30 pts
* **Controlled Fix & Verification:** 25 pts
* **Technical Report & Presentation:** 15 pts

<!--
Notas del orador (160–180 min):
- Modera presentaciones de 3 minutos + 1 pregunta técnica por equipo.
- Al terminar, asegúrate de que todos restauran el snapshot `BASELINE – BEFORE WORKSHOP`.
-->
