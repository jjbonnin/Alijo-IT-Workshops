---
marp: true
theme: default
paginate: true
backgroundColor: #0f172a
color: #f8fafc
header: "Alijó IT Workshops | Workshop 3: Build and Configure a Network"
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

![bg opacity:0.35](../../Workshop-1-IT-Troubleshooting-Challenge/Assets/slides/cover-w3.jpg)

# Workshop 3: Build and Configure a Networ

### Practical Approaches to IT Projects and Problem-Solving

**Agrupamento de Escolas D. Sancho II, Alijó**

*Ponente: Juan José Bonnín Sansó (IES Sa Colomina)*

---

## 0. Workshop 3: Build and Configure a Network
### Practical Approaches to IT Projects and Problem-Solving
**Alijó IT Workshops**

* **Duration:** 180 Minutes (3 Hours)
* **Format:** Team-based Hybrid Lab (Simulation + Physical Bench)
* **Tools:** Cisco Packet Tracer + Physical Switches, Routers, Cat5e/Cat6 & Ubuntu Server

> **Visual / Imagen recomendada (Portada):**
> *Ilustración técnica limpia sobre fondo azul oscuro mostrando dos subredes (`Admin` y `Operations`) conectadas a través de un router central hacia un servidor local.*
> *Prompt IA sugerido:* `"Minimalist dark-blue network architecture presentation cover illustration, two small office subnets connected through a central router to an Ubuntu local server, glowing cyan Ethernet links, clean flat vector style, no text"`

<!--
Notas del orador (00–05 min):
- Presenta el objetivo del taller: pasar del plano lógico en papel y Packet Tracer al cableado y configuración real de una red física de pequeña empresa.
-->

---

## 1. Mission & Learning Outcomes

By the end of this 3-hour workshop, your team will be able to:

1. **Design a segmented IPv4 addressing plan** (`192.168.10.0/24` and `192.168.20.0/24`) without IP conflicts.
2. **Build, configure, and validate a multi-subnet topology** in Cisco Packet Tracer.
3. **Assemble and test a physical Ethernet bench** using structured cabling and static IPv4 settings.
4. **Deploy local HTTP (`8080/tcp`) and DNS (`dnsmasq`) services** protected by `ufw`.
5. **Compare simulated vs. physical behavior** and troubleshoot Layer 1–7 network faults.

> **Visual / Imagen recomendada:**
> *Esquema comparativo en 3 fases: `[1. Diseño IPv4]` ➔ `[2. Simulación Packet Tracer]` ➔ `[3. Red Física + Servidor Ubuntu]`.*

<!--
Notas del orador (05–10 min):
- Destaca que el paso más valioso es entender por qué algo que funciona en Packet Tracer puede fallar en la mesa física (cable cruzado/dañado, máscara errónea, firewall del host).
-->

---

## 2. Three-Hour Session Roadmap (180 Min)

| Block | Duration | Activity | Team Deliverable |
| :--- | :--- | :--- | :--- |
| **1** | 15 min | Briefing, physical bench safety & team roles | Roles assigned |
| **2** | 20 min | IPv4 Subnetting & Topology Design | `Network-Design-Plan.md` |
| **3** | 45 min | **Phase A:** Cisco Packet Tracer Build & Ping/Web Tests | `.pkt` verified |
| **4** | 50 min | **Phase B:** Physical Bench Assembly & Ubuntu Server Setup | Live `HTTP 200 OK` |
| **5** | 30 min | **Phase C:** Live Fault Injection & Troubleshooting | Faults resolved |
| **6** | 20 min | Environment comparison, teardown & debrief | `Final-Report.md` |

> **Visual / Imagen recomendada:**
> *Línea de tiempo en dos carriles paralelos mostrando el flujo de 45 min en Packet Tracer seguido de 50 min en hardware real.*

<!--
Notas del orador (10–12 min):
- Recuerda que en el bloque 6 deben dejar la mesa física recogida y restaurada a sus valores por defecto.
-->

---

## 3. Team Roles & Physical Bench Safety

### Team Roles (4–5 Students)
* **Network Architect:** Maintains the IPv4 plan, VLAN/subnet boundaries, and gateway table.
* **Simulation Lead:** Builds and tests the topology in Cisco Packet Tracer.
* **Physical Cabling & Switch Tech:** Verifies link LEDs, patch cords, and interface names (`ip -br link`).
* **Server & Firewall Admin:** Configures static IPv4, HTTP (`8080`), `dnsmasq`, and `ufw` on Ubuntu.
* **Test & Evidence Recorder:** Runs `ping`, `dig`, and `curl` acceptance tests and logs outputs.

### Physical Safety Rules
1. **Isolated Lab Gear Only:** Never plug lab switches/routers into classroom wall jacks or campus Wi-Fi.
2. **Inspect Cables First:** Check RJ45 clips and link LEDs before debugging Layer 3 routing.
3. **Power & ESD Care:** Keep liquids away from switches and power strips.

> **Visual / Imagen recomendada:**
> *Foto real o diagrama de un switch de sobremesa con LEDs de enlace en verde (`Link/Act`) junto a un cable UTP etiquetado.*

<!--
Notas del orador (12–15 min):
- Insiste mucho en la Regla 1: jamás conectar un router o servidor DHCP del laboratorio a la roseta de red del centro educativo.
-->

---

![bg right:42% contain](../../Workshop-3-Build-and-Configure-Network/Assets/slides/diagram-topology.jpg)

## 4. Reference Topology & IPv4 Addressing Plan

```text
  [Subnet A: Admin / Servers]                [Subnet B: Client Workstations]
       192.168.10.0/24                                192.168.20.0/24
              │                                              │
   ┌──────────┴──────────┐                        ┌──────────┴──────────┐
   │  Switch SW1 (A)     │                        │  Switch SW2 (B)     │
   └────┬───────────┬────┘                        └────┬───────────┬────┘
        │           │                                  │           │
  [.10 Server]  [.1 Router G0/0] ◄── Router ──► [.1 Router G0/1]  [.20 Client PC]
```

| Device / Role | Interface | IPv4 Address | Subnet Mask | Default Gateway |
| :--- | :--- | :--- | :--- | :--- |
| **Router (LAN A)** | `Gig0/0` | `192.168.10.1` | `255.255.255.0` (`/24`) | — |
| **Router (LAN B)** | `Gig0/1` | `192.168.20.1` | `255.255.255.0` (`/24`) | — |
| **Lab Server (Ubuntu)** | `NIC` | `192.168.10.10` | `255.255.255.0` (`/24`) | `192.168.10.1` |
| **Admin Workstation** | `NIC` | `192.168.10.20` | `255.255.255.0` (`/24`) | `192.168.10.1` |
| **Operations Client** | `NIC` | `192.168.20.20` | `255.255.255.0` (`/24`) | `192.168.20.1` |

> **Visual / Imagen recomendada:**
> *Captura limpia de la topología montada en Cisco Packet Tracer con etiquetas visibles para cada subred.*

<!--
Notas del orador (15–35 min):
- Pide a los equipos que completen su tabla de direccionamiento antes de arrastrar dispositivos en Packet Tracer.
-->

---

## 5. Phase A: Cisco Packet Tracer Simulation (45 Min)

Build and validate the full topology in **Cisco Packet Tracer**:

1. **Place & Cable Devices:** 1 Router (`2911`/`4321`), 2 Switches (`2960`), 1 Server, and 2–3 PCs using copper straight-through cables.
2. **Enable Router Interfaces:** Configure IP addresses on `Gig0/0` and `Gig0/1` and execute `no shutdown`.
3. **Configure End Hosts:** Assign static IPv4, `/24` mask, default gateway, and DNS server (`192.168.10.10`).
4. **Enable Server Services:** Turn on **HTTP** and add an **A Record** in **DNS** (`intranet.alijo.local` ➔ `192.168.10.10`).
5. **Acceptance Test:** From `192.168.20.20`, open the Packet Tracer browser and load `http://intranet.alijo.local`.

> **Visual / Imagen recomendada:**
> *Captura de Packet Tracer mostrando el navegador web del PC cliente cargando `intranet.alijo.local` tras configurar el registro DNS A.*

<!--
Notas del orador (35–80 min):
- Error típico en Packet Tracer: olvidar `no shutdown` en las interfaces del router (triángulos rojos) o no configurar el servidor DNS en los PCs clientes.
-->

---

## 6. Phase B: Physical Bench & Ubuntu Server Setup (50 Min)

Move from simulation to real hardware on your lab bench:

### 1. Static IPv4 on Ubuntu Server Host
```bash
ip -br link                                   # Identify NIC (e.g., enp3s0)
sudo ip addr flush dev <IFACE>
sudo ip addr add 192.168.10.10/24 dev <IFACE>
sudo ip link set <IFACE> up
sudo ip route add default via 192.168.10.1
```

### 2. Local HTTP Intranet (`8080/tcp`) & DNS (`dnsmasq`)
```bash
nohup python3 -m http.server 8080 --directory ~/alijo-intranet > /tmp/alijo-http.log 2>&1 &
dig @192.168.10.10 intranet.alijo.local +short   # Expected: 192.168.10.10
```

> **Visual / Imagen recomendada:**
> *Captura de terminal mostrando `ip -br -4 addr` con `192.168.10.10/24 UP` y la respuesta de `dig @192.168.10.10 intranet.alijo.local +short`.*

<!--
Notas del orador (80–115 min):
- Acompaña a los equipos en la identificación del nombre real de su tarjeta de red (`enp3s0`, `ens33`, etc.) antes de ejecutar `ip addr flush`.
-->

---

## 7. Host Firewall (`ufw`) & End-to-End Verification

Never leave the physical server unprotected during testing:

```bash
sudo ufw --force enable
sudo ufw allow from 192.168.10.0/24 to any port 8080 proto tcp
sudo ufw allow from 192.168.10.0/24 to any port 53
sudo ufw status numbered
```

### Client End-to-End Acceptance Checklist
1. **Layer 2/3 Local:** `ping -c 3 192.168.10.1` (Default gateway reachable)
2. **Layer 3 Server:** `ping -c 3 192.168.10.10` (Server IP reachable)
3. **Layer 7 DNS:** `dig @192.168.10.10 intranet.alijo.local +short` ➔ `192.168.10.10`
4. **Layer 7 HTTP:** `curl -I http://intranet.alijo.local:8080` ➔ `HTTP/1.0 200 OK`

> **Visual / Imagen recomendada:**
> *Captura de pantalla de `sudo ufw status numbered` junto a la salida `HTTP/1.0 200 OK` de `curl -I`.*

<!--
Notas del orador (115–130 min):
- Si usan dos subredes físicas (`192.168.10.0/24` y `192.168.20.0/24`), recuerda que deberán permitir también tráfico desde `192.168.20.0/24` en `ufw`.
-->

---

## 8. Simulated vs. Physical Network: Key Differences

Why is testing on real hardware essential even after a green Packet Tracer lab?

| Aspect | Cisco Packet Tracer | Physical Lab Bench |
| :--- | :--- | :--- |
| **Physical Layer (L1)** | Virtual links never suffer loose RJ45 clips or bad crimps | Physical link LEDs, duplex negotiation, and cable faults matter |
| **Interface Naming** | Standardized (`Gig0/0`, `FastEthernet0`) | Hardware-dependent (`enp3s0`, `ens33`, `eth0`) |
| **Host Firewalls** | End devices have no OS firewall enabled by default | Ubuntu `ufw` actively drops unpermitted ports (`8080`, `53`) |
| **Service Daemons** | Toggle switches ("HTTP On", "DNS On") | Real Linux processes (`python3`, `dnsmasq`) & port bindings |

> **Visual / Imagen recomendada:**
> *Tabla visual comparativa con iconos de simulación virtual vs. hardware real.*

<!--
Notas del orador (130–135 min):
- Esta tabla ayuda directamente a los alumnos a completar la sección de comparación de su `Final-Report.md`.
-->

---

## 9. Phase C: Network Fault Troubleshooting (30 Min)

Diagnose injected network faults strictly from **Layer 1 up to Layer 7**:

```text
[L1: Link LEDs / ip link] ──▶ [L3: IP / Mask / Gateway] ──▶ [L4: ufw / ss -tulpn] ──▶ [L7: dig / curl]
```

### Common Faults to Watch For
* **Wrong Subnet Mask (`/16` vs `/24`):** Causes host to treat remote subnets as local ARP targets.
* **Missing Default Gateway:** Local subnet pings work, cross-subnet routing fails (`Network is unreachable`).
* **Firewall Block (`ufw`):** `ping` succeeds (ICMP), but `curl :8080` or `dig` times out.
* **DNS Misconfiguration:** `http://192.168.10.10:8080` works, `http://intranet.alijo.local:8080` fails.

> **Visual / Imagen recomendada:**
> *Diagrama en escalera de 4 peldaños (`L1 Física` ➔ `L3 Red/IP` ➔ `L4 Transporte/Firewall` ➔ `L7 Aplicación/DNS`).*

<!--
Notas del orador (135–160 min):
- Inyecta 2 o 3 fallos reales de `Fault-Injection-and-Recovery.md` (por ejemplo, puerta de enlace errónea o regla `ufw` bloqueando el puerto `8080`).
-->

---

## 10. Teardown, Cleanup & Evaluation (20 Min)

### Mandatory Server Cleanup Before Leaving
```bash
pkill -f "http.server 8080" || true
rm -rf ~/alijo-intranet /tmp/alijo-http.log
sudo rm -f /etc/dnsmasq.d/alijo-lab.conf
sudo systemctl stop dnsmasq 2>/dev/null || true
sudo ufw --force reset
sudo nmcli networking off && sudo nmcli networking on
```

### Grading Rubric (100 Points)
* **IPv4 Addressing & Topology Design:** 20 pts
* **Packet Tracer Simulation & Verification:** 25 pts
* **Physical Lab Assembly, Services & `ufw`:** 25 pts
* **Fault Troubleshooting & Final Report:** 30 pts

<!--
Notas del orador (160–180 min):
- Supervisa que todos los equipos ejecuten los comandos de limpieza en el servidor Ubuntu y desconecten ordenadamente los latiguillos de red.
-->
