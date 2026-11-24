# Guía de Entregas y Evaluación Cruzada (Peer-to-Peer)
**Alijó IT Workshops | Grupos A1–A6 y B1–B6**

---

## 1. Flujo de Trabajo de Cada Taller

1. **Validación del Entorno (`Tarea 0`):** Antes de comenzar, cada equipo abre un Issue con la plantilla **Tarea 0** para verificar su VM Ubuntu, el snapshot base (`BASELINE – BEFORE WORKSHOP`) y los requisitos específicos de su taller (`W1`–`W4`).
2. **Desarrollo Práctico en Equipo:** Completad las hojas de trabajo (`Worksheets/`) y las pruebas técnicas correspondientes al taller asignado dentro de vuestro entorno aislado.
3. **Entrega del Taller (`Tarea 1` a `Tarea 4`):** Al finalizar la sesión, el coordinador del equipo abre un Issue con la plantilla del taller correspondiente (`[TAREA-X][Grupo-XX]`) pegando los resultados y evidencias verificadas.
4. **Auditoría Cruzada Rotativa (`Peer-to-Peer`):** Cada equipo revisa el Issue del grupo que le corresponde según la tabla de rotación por tarea y publica su evaluación técnica comentando `PEER-SCORE: XX` (valor entre `0` y `100`).

---

## 2. Tabla de Rotación de Revisiones Cruzadas por Tarea

Para evitar que dos grupos se evalúen siempre entre sí, **el grupo evaluado cambia en cada taller**:

### Turno A (`A1` – `A6`)
| Grupo Auditor | Tarea 1 (W1) | Tarea 2 (W2) | Tarea 3 (W3) | Tarea 4 (W4) |
| :---: | :---: | :---: | :---: | :---: |
| **`A1`** | Revisa a `A2` | Revisa a `A3` | Revisa a `A4` | Revisa a `A5` |
| **`A2`** | Revisa a `A3` | Revisa a `A4` | Revisa a `A5` | Revisa a `A6` |
| **`A3`** | Revisa a `A4` | Revisa a `A5` | Revisa a `A6` | Revisa a `A1` |
| **`A4`** | Revisa a `A5` | Revisa a `A6` | Revisa a `A1` | Revisa a `A2` |
| **`A5`** | Revisa a `A6` | Revisa a `A1` | Revisa a `A2` | Revisa a `A3` |
| **`A6`** | Revisa a `A1` | Revisa a `A2` | Revisa a `A3` | Revisa a `A4` |

### Turno B (`B1` – `B6`)
| Grupo Auditor | Tarea 1 (W1) | Tarea 2 (W2) | Tarea 3 (W3) | Tarea 4 (W4) |
| :---: | :---: | :---: | :---: | :---: |
| **`B1`** | Revisa a `B2` | Revisa a `B3` | Revisa a `B4` | Revisa a `B5` |
| **`B2`** | Revisa a `B3` | Revisa a `B4` | Revisa a `B5` | Revisa a `B6` |
| **`B3`** | Revisa a `B4` | Revisa a `B5` | Revisa a `B6` | Revisa a `B1` |
| **`B4`** | Revisa a `B5` | Revisa a `B6` | Revisa a `B1` | Revisa a `B2` |
| **`B5`** | Revisa a `B6` | Revisa a `B1` | Revisa a `B2` | Revisa a `B3` |
| **`B6`** | Revisa a `B1` | Revisa a `B2` | Revisa a `B3` | Revisa a `B4` |

---

## 3. Sistema de Calificación Híbrida

* **Modalidad Estándar (sin intervención docente):**
  * **60% Evaluación Automática** (verificación de estructura, comandos, evidencias y seguridad operativa).
  * **40% Evaluación Peer-to-Peer** (`PEER-SCORE: XX` emitido por el grupo revisor asignado para esa tarea).
* **Modalidad con Revisión Docente (`teacher-review`):**
  * **30% Evaluación Automática** + **30% Peer-to-Peer** + **40% Profesor** (`TEACHER-SCORE: XX`).
* **Nota mínima de superación:** **70 / 100 puntos**.

---

## 4. Rúbrica Rápida para el Grupo Auditor (`PEER-SCORE`)

Antes de publicar vuestro comentario `PEER-SCORE: XX` en el Issue del grupo asignado, comprobad estos 4 criterios (25 puntos cada uno):

1. **Trazabilidad y Evidencias Reales (25 pts):** Las salidas de terminal (`systemctl`, `ip`, `dig`, `curl`, `ufw`, etc.) son reales, legibles y corresponden al problema planteado.
2. **Metodología y Causa Raíz (25 pts):** Se distingue claramente entre síntomas observados, causa raíz diagnosticada y solución aplicada.
3. **Verificación Post-Cambio (25 pts):** Existen pruebas objetivas posteriores al cambio que demuestran que el servicio funciona correctamente.
4. **Seguridad e Higiene de Laboratorio (25 pts):** Se respetó el aislamiento de red y no se aplicaron atajos inseguros (`chmod 777`, `ufw disable`, login directo como `root` o exposición de credenciales).

> **Regla Anti-Autoevaluación:** El bot comprueba automáticamente el grupo revisor correspondiente a cada tarea. Ningún integrante del propio grupo evaluado ni de un grupo distinto al revisor asignado puede emitir `PEER-SCORE`.
