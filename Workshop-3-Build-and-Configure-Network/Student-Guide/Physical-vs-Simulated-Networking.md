# Physical vs. Simulated Networking
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## 1. Why Build in Both Environments?
Professional network engineers rarely deploy changes directly onto live production hardware without validating the design first. In Workshop 3, you will build the same small-business topology twice:
1. **Simulated Environment (Cisco Packet Tracer):** Ideal for rapid prototyping, visualizing packet flow in *Simulation Mode*, testing routing and DHCP/DNS logic, and safely breaking configurations without physical constraints.
2. **Physical Lab Environment (Real Switches, Routers & Ubuntu Hosts):** Essential for experiencing genuine Layer 1 cabling issues, NIC driver/link negotiation, OS firewall interactions, real service daemons, and live hardware troubleshooting.

---

## 2. Side-by-Side Comparison: Packet Tracer vs. Physical Hardware

| Dimension | Cisco Packet Tracer (Simulation) | Physical Lab Hardware (Real World) |
| :--- | :--- | :--- |
| **Layer 1 (Cabling & Media)** | Simplified virtual cables; no EMI interference, broken RJ45 clips, or bad patch panels. Auto-MDIX is predictable, though older devices still enforce straight-through vs. crossover rules. | Physical faults are common: damaged Cat5e/Cat6 cables, bent pins, loose RJ45 jacks, unpowered switches, or mismatched duplex/speed negotiation. |
| **Interface Naming & OS Behavior** | Standardized Cisco IOS interface names (`GigabitEthernet0/0`, `FastEthernet0/1`) and simplified desktop IP dialog boxes. | Real Linux/Windows OS interfaces (`ens33`, `enp3s0`, `eth0`), NetworkManager/Netplan profiles, and vendor-specific router web/CLI interfaces. |
| **Packet Visibility** | Built-in **Simulation Mode** visually animates ARP, ICMP, DHCP, DNS, and HTTP PDUs hop-by-hop with color-coded envelopes. | Packets are invisible unless captured actively on an interface or SPAN/mirror port using `tcpdump` or Wireshark. |
| **Performance & Timing** | Instantaneous switching/routing unless stepped manually in Simulation Mode; artificial convergence timers. | Real propagation delay, Spanning Tree Protocol (STP) 30–50 second port listening/learning delays, and real ARP/DNS cache TTLs. |
| **Security & Host Firewalls** | End-device PCs have no active OS firewall blocking ICMP/HTTP by default unless explicitly configured. | Ubuntu/Windows hosts run active firewalls (`ufw`, `nftables`, Windows Defender Firewall) that frequently block `ping` or inbound HTTP/SSH ports. |
| **Reset & Recovery** | Instantaneous **Undo**, **Reset Activity**, or reopening the `.pkt` file restores the exact baseline state. | Requires manually reverting configuration files, flushing IP/route tables, restarting services, or restoring VM snapshots. |

---

## 3. Key Real-World Surprises When Moving from Simulation to Hardware
When transitioning your validated Packet Tracer design onto physical lab equipment, watch out for these four common differences:
1. **Spanning Tree Protocol (STP) Delay:** On real managed switches, plugging in a patch cable does not forward traffic immediately—it can take up to 30 seconds for the switch port LED to transition from amber to green unless PortFast is enabled.
2. **Host Firewall Blocking ICMP (`ping`):** A Windows or Ubuntu host may be properly connected at Layer 3 yet still fail to reply to `ping` because local firewall rules drop ICMP Echo Requests.
3. **DNS Caching & `/etc/hosts`:** Real operating systems cache negative and positive DNS lookups (`systemd-resolved`) and check `/etc/hosts` before querying external DNS servers.
4. **Physical Port Mismatches:** In Packet Tracer, hovering over a link immediately shows `Fa0/1` or `Gi0/0`; on real switches and routers, you must trace physical patch cables and verify port labels and link LEDs directly on the chassis.

---

## 4. Reflection Link to Your Lab Worksheet
During the physical and simulated lab phases, record at least **four concrete behavioral differences** you observe in `Worksheets/Environment-Comparison-Worksheet.md`.
