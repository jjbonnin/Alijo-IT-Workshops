# Instructor Guide — Workshop 3: Build and Configure a Network
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

---

## 1. Instructor Overview & Pedagogical Goals
Workshop 3 bridges conceptual TCP/IP networking with hands-on implementation across two complementary environments: **Cisco Packet Tracer** and **physical Ethernet bench hardware**. Rather than treating simulation and physical labs as isolated exercises, students first design and validate a two-subnet small-business topology (`192.168.10.0/24` and `192.168.20.0/24`) in Packet Tracer, replicate core Layer 1–7 connectivity on real switches and Ubuntu hosts, compare behavioral differences, and finally resolve two injected troubleshooting tickets.

---

## 2. Recommended 180-Minute Pacing Plan

| Time | Duration | Phase | Instructor Actions & Facilitation Notes |
| :--- | :--- | :--- | :--- |
| **00:00–00:15** | 15 min | **Briefing & Topology Design** | Present the small-business scenario (`LAN A` Office + `LAN B` Servers). Teams complete `Topology-Design-Worksheet.md` and `IP-Addressing-Worksheet.md`. |
| **00:15–00:30** | 15 min | **Design Gate Check** | Quickly verify each team's IP table before they touch Packet Tracer (check for duplicate IPs, wrong gateway subnets, or DHCP pool overlap). |
| **00:30–01:15** | 45 min | **Phase 1: Packet Tracer Build** | Guide students through `Packet-Tracer-Guide.md`. Highlight why `ip helper-address 192.168.20.10` is required on `R1 Gi0/0` for `PC2` to receive DHCP across subnets. |
| **01:15–02:00** | 45 min | **Phase 2: Physical Network Lab** | Teams wire physical switches, routers/gateways, and Ubuntu hosts (`Physical-Network-Lab-Guide.md`), configure static IPs, start the local HTTP server, and log tests. |
| **02:00–02:15** | 15 min | **Environment Comparison** | Facilitate a brief discussion as teams complete `Environment-Comparison-Worksheet.md` (STP port convergence delay, `ufw` ICMP filtering, real cable link states). |
| **02:15–02:50** | 35 min | **Phase 3: Troubleshooting Challenge** | Distribute the faulted `.pkt` file (`Ticket A`) and run the Ubuntu fault injection script (`Ticket B`). Enforce Bottom-Up diagnostics and forbid `ufw disable`. |
| **02:50–03:00** | 10 min | **Debrief & Bench Reset** | Review root causes with the class, collect `Incident-Report-Template.md`, and verify all Ubuntu machines and switches are restored to baseline. |

---

## 3. Pre-Class Preparation Checklist
1. **Workstation Software:** Verify Cisco Packet Tracer launches cleanly on all student machines and `Assets/Small-Business-Network.pkt` is accessible.
2. **Physical Bench Hardware:** Test all Cat5e/Cat6 patch cables, switch power adapters, and router/gateway LAN ports ahead of time (keep 2–3 intentionally faulty/unplugged cables separate for optional physical Layer 1 demos).
3. **Ubuntu Host Snapshots:** Confirm every Ubuntu lab VM/workstation has a clean `BASELINE – BEFORE WORKSHOP` snapshot and `python3`, `iproute2`, `dnsutils`, `curl`, and `ufw` installed.
4. **Fault Assets Ready:** Prepare the broken Packet Tracer file (`Small-Business-Network-Fault.pkt`) and review `Solutions-and-Setup/Fault-Injection-and-Recovery.md` before class.

---

## 4. Common Student Pitfalls & Coaching Tips
* **Forgetting `ip helper-address` on `R1`:** Students configure the DHCP pool on `Server-Core` (`192.168.20.10`), but `PC2` (`192.168.10.0/24`) gets an APIPA address (`169.254.x.x`). Ask them: *"What happens to a Layer 2 DHCP Discover broadcast when it hits a router interface?"*
* **Impatience with Switch STP:** In Packet Tracer, ports stay amber for ~30 seconds after cabling. Encourage students to check link status rather than immediately deleting cables, and connect this directly to real switch behavior in Phase 2.
* **Disabling `ufw` During Troubleshooting:** Remind students that in production environments, turning off a host firewall is a security violation; require a targeted `ufw allow` rule instead.
* **Changing Multiple Settings at Once:** Require teams to verbalize their hypothesis and expected test result before executing any fix command.
