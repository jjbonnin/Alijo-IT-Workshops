---
marp: true
theme: default
paginate: true
backgroundColor: #0f172a
color: #f8fafc
header: "Alijó IT Workshops | Workshop 2: AI as an IT Technician Assistant"
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

![bg opacity:0.35](../../Workshop-1-IT-Troubleshooting-Challenge/Assets/slides/cover-w2.jpg)

# Workshop 2: AI as an IT Technician Assistant

### Practica2 Artificial Intelligence and its Applications in IT

**Agrupamento de Escolas D. Sancho II, Alijó**

*Ponente: Juan José Bonnín Sansó (IES Sa Colomina)*

---

## 0. Workshop 2: AI as an IT Technician Assistant
### Practical Approaches to IT Projects and Problem-Solving
**Alijó IT Workshops**

* **Duration:** 180 Minutes (3 Hours)
* **Format:** Team-based Hands-On Lab (4–5 students per team)
* **Environment:** Ubuntu Desktop VM + Approved AI Assistant

> **Visual / Imagen recomendada (Portada):**
> *Ilustración limpia en tonos azul noche y cian mostrando una terminal Linux a la izquierda y un asistente de IA a la derecha conectados por un icono de escudo/verificación.*
> *Prompt IA sugerido:* `"Minimalist dark-blue tech presentation cover illustration, Linux terminal window on the left connected to an AI assistant node through a security verification shield icon, clean flat vector style, no text"`

<!--
Notas del orador (00–05 min):
- Da la bienvenida al Taller 2 y plantea la idea central: la IA es un copiloto muy rápido, pero no tiene acceso real a tu máquina ni asume responsabilidad si un comando borra datos.
- El técnico sigue siendo el piloto responsable de cada comando que entra en la terminal.
-->

---

## 1. Mission & Learning Outcomes

By the end of this 3-hour workshop, your team will be able to:

1. **Craft Evidence-First Prompts** containing real OS context, error logs, and safety constraints.
2. **Audit AI-generated commands and scripts** line by line *before* execution.
3. **Detect AI hallucinations, deprecated flags, and dangerous shortcuts** (`rm -rf`, `chmod 777`, `curl | bash`).
4. **Debug broken Python/Bash utilities** iteratively using real execution tracebacks.
5. **Document every AI interaction and verification test** transparently in an audit log.

> **Visual / Imagen recomendada:**
> *Esquema en 4 pasos: `[1. Evidencia Real]` ➔ `[2. Prompt Estructurado]` ➔ `[3. Auditoría Pre-Ejecución]` ➔ `[4. Prueba en VM]`.*

<!--
Notas del orador (05–10 min):
- Recalca que copiar y pegar a ciegas desde el chat a la terminal es la causa número uno de incidentes graves con asistentes de IA.
-->

---

## 2. Three-Hour Session Roadmap (180 Min)

| Block | Duration | Activity | Team Deliverable |
| :--- | :--- | :--- | :--- |
| **1** | 15 min | Briefing, AI safety rules & team role assignment | Roles assigned |
| **2** | 25 min | Evidence-First Prompting & Pre-Execution Audit rules | Method check |
| **3** | 20 min | VM Baseline & Scenario asset inspection | Baseline ready |
| **4** | 65 min | **4 Progressive AI Scenarios** (Logs, Python, Safety Trap, Admin) | `Prompt-Record.md` |
| **5** | 35 min | Final verification & AI Audit Report completion | `Final-Report.md` |
| **6** | 20 min | Team debriefs & lessons learned | 3-min pitch |

> **Visual / Imagen recomendada:**
> *Barra de progreso horizontal con 6 bloques destacando los 65 minutos de práctica sobre los 4 escenarios.*

<!--
Notas del orador (10–12 min):
- Advierte de que uno de los escenarios contiene una trampa deliberada de seguridad para comprobar si auditan antes de ejecutar.
-->

---

![bg right:42% contain](../../Workshop-2-AI-IT-Technician-Assistant/Assets/slides/diagram-ai-audit.jpg)

## 3. Team Roles & AI Governance

Every team (4–5 members) divides responsibility to prevent blind execution:

* **Team Coordinator:** Enforces timeboxes and ensures the team reviews every AI output before running it. *(Combines with Reporter in teams of 4)*.
* **Prompt Engineer:** Writes structured, context-rich prompts using real CLI outputs (never sensitive credentials).
* **Security & Code Auditor:** Inspects every AI-suggested command/script for destructive flags, hardcoded secrets, or side effects.
* **Lead Technician:** Executes **only approved** commands in the Ubuntu VM and captures outputs.
* **Reporter:** Documents prompts, AI flaws caught, fixes, and final proof.

> **Visual / Imagen recomendada:**
> *Diagrama de control: el `Security & Code Auditor` actúa como barrera ("Gatekeeper") entre la respuesta de la IA y la terminal del `Lead Technician`.*

<!--
Notas del orador (12–15 min):
- Insiste en que ningún comando generado por IA puede ejecutarse sin el visto bueno explícito del Security & Code Auditor del equipo.
-->

---

## 4. Non-Negotiable AI Safety Rules

1. **Snapshot First:** Verify `BASELINE – BEFORE WORKSHOP` exists in VirtualBox before starting.
2. **Never Paste Blindly:** Read every flag (`man <cmd>` or `<cmd> --help`) before running an AI command.
3. **Zero Blind Pipe-to-Shell:** Never run `curl ... | sudo bash` or download unverified third-party scripts.
4. **No Destructive Shortcuts:** Reject any AI suggestion using `chmod 777`, `ufw disable`, or recursive `rm -rf` on system folders.
5. **Protect Secrets & PII:** Never paste real passwords, private SSH keys, or personal data into external AI chats.

> **Visual / Imagen recomendada:**
> *Tabla visual de semáforo: Verde (`--dry-run`, `man`, pruebas en `/tmp`), Amarillo (`sudo systemctl reload`), Rojo (`chmod 777`, `rm -rf /`, `curl | sh`).*

<!--
Notas del orador (15–20 min):
- Muestra un ejemplo real de cómo una IA puede inventar un parámetro inexistente o sugerir `chmod 777` para "arreglar rápido" un error de permisos.
-->

---

## 5. Anatomy of an Evidence-First Prompt

Stop asking vague questions (*"Why doesn't my script work?"*). Use the **4-Part Context Formula**:

```text
1. [ENVIRONMENT]  Ubuntu 22.04 LTS, Python 3.10, non-root user with sudo.
2. [SYMPTOM/LOGS] Exact command run + verbatim stderr/traceback output.
3. [CONSTRAINTS]  Must keep ufw enabled, no chmod 777, explain each flag.
4. [OUTPUT ASK]   Give a minimal diagnostic check first before any fix.
```

* **Result:** Accurate, reproducible answers instead of generic guesses.

> **Visual / Imagen recomendada:**
> *Comparativa lado a lado: Prompt pobre (1 línea vaga) vs. Prompt estructurado en 4 bloques etiquetados.*

<!--
Notas del orador (20–35 min):
- Pide a los equipos que usen exactamente esta plantilla de 4 bloques en su primera consulta del Escenario 1.
-->

---

![bg right:42% contain](../../Workshop-2-AI-IT-Technician-Assistant/Assets/slides/diagram-ai-audit.jpg)

## 6. The Pre-Execution Audit Checklist

Before pressing **Enter** on any AI-generated snippet, verify **5 questions**:

| Check | Question to Ask | Red Flag Example |
| :--- | :--- | :--- |
| **1. Scope** | Does it touch only the intended files/services? | `rm -rf *` run in the wrong directory |
| **2. Flags** | Do all flags actually exist in this Ubuntu version? | Hallucinated CLI options |
| **3. Privileges** | Does it really need `sudo`, or can it run as user? | Running a Python parser as `root` |
| **4. Permissions** | Does it follow least privilege (`640`/`644`/`750`)? | Suggesting `chmod 777` |
| **5. Reversibility** | Can we undo it or test with `--dry-run` first? | Overwriting configs without `.bak` |

> **Visual / Imagen recomendada:**
> *Captura de terminal mostrando un comando con `--dry-run` o `cp config.conf config.conf.bak` antes de editar.*

<!--
Notas del orador (35–40 min):
- Recuerda que en el `Prompt-and-Results-Record.md` deben anotar qué revisaron antes de ejecutar cada bloque.
-->

---

## 7. Workshop Scenarios Overview (65 Min)

Your team will work through **4 progressive scenarios**:

1. **Scenario 01 — Log & Service Triage:** Feed real `journalctl` / service errors to AI to isolate a failing background service without breaking dependencies.
2. **Scenario 02 — Debugging `diagnostic_script.py`:** Use AI to identify syntax, logic, and exception-handling bugs in a broken Python monitoring script, then verify locally.
3. **Scenario 03 — The AI Safety Trap:** Evaluate an AI-proposed remediation plan containing subtle security flaws and destructive commands — **catch and rewrite it safely**.
4. **Scenario 04 — Automated Admin Task:** Co-design a clean, idempotent Bash health check with AI and validate edge cases.

> **Visual / Imagen recomendada:**
> *4 tarjetas numeradas con iconos: `[01 Logs]`, `[02 Python Debug]`, `[03 Safety Trap ⚠️]`, `[04 Bash Script]`.*

<!--
Notas del orador (40–105 min):
- Supervisa especialmente el Escenario 03: observa qué equipos detectan la trampa sin ejecutarla y qué equipos necesitan una pregunta guía.
-->

---

## 8. Iterative Debugging Loop with AI

When AI-generated code fails on the first run:

```text
[Run Code in VM] ──▶ [Capture Exact Traceback] ──▶ [Feed Error + Line # to AI]
        ▲                                                      │
        └────────── [Audit Diff & Re-Test Locally] ◀───────────┘
```

* **Never say:** *"It still gives an error, fix it."*
* **Always provide:** Exact line number, full traceback, and what changed since the previous test.

> **Visual / Imagen recomendada:**
> *Captura de terminal mostrando un `Traceback` de Python con el número de línea resaltado.*

<!--
Notas del orador (70–90 min):
- Refuerza este flujo durante el Escenario 02 (`diagnostic_script.py`), donde suelen aparecer 2 o 3 errores encadenados.
-->

---

## 9. Documentation & Grading Rubric (100 Points)

Your `Prompt-and-Results-Record.md` and `Final-Report.md` must prove **critical human oversight**:

* **Evidence-First Prompting Quality:** 25 pts
* **Pre-Execution Security & Accuracy Audit:** 30 pts
* **Technical Execution & Verification Proof:** 25 pts
* **Critical Reflection & Final Report:** 20 pts

> **Automatic Penalty (-15 pts):** Executing destructive or insecure AI commands (`chmod 777`, disabling firewalls, unverified `rm -rf`) without catching them during the audit.

<!--
Notas del orador (105–180 min):
- Dedica los últimos 20 minutos a que cada equipo muestre un fallo o alucinación real que haya cazado a la IA durante la sesión.
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
