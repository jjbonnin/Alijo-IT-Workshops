# Workshop 3: Build and Configure a Network
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

---

## 1. Workshop Overview
This hands-on workshop guides students through designing, addressing, building, and troubleshooting a small business network across both a **simulated environment (Cisco Packet Tracer)** and a **physical lab network** (switches, routers/gateways, Ethernet cabling, and Ubuntu/client endpoints). Teams plan IPv4 subnets, configure interfaces and local services (DHCP, DNS, HTTP), verify end-to-end connectivity, compare simulated versus real-world hardware behavior, and resolve injected network faults.

---

## 2. Learning Objectives
By the end of this 3-hour session, participants will be able to:
1. Design a structured small-business network topology with clear device roles, cabling types, and IPv4 addressing schemes.
2. Calculate and assign valid IPv4 host addresses, subnet masks, default gateways, and DNS servers without conflicts.
3. Build and configure a functional multi-device network in **Cisco Packet Tracer** (`Assets/Small-Business-Network.pkt`) and replicate core connectivity on **physical networking equipment**.
4. Verify Layer 1–7 connectivity using `ip`, `ping`, `traceroute`, `nslookup`/`dig`, and `curl`.
5. Identify key behavioral differences between simulated Packet Tracer models and physical network hardware.
6. Diagnose and resolve IP addressing, cabling/VLAN, gateway, and service faults using a structured troubleshooting workflow.

---

## 3. Repository Structure for Workshop 3

```text
Workshop-3-Build-and-Configure-Network/
├── README.md                                          # Workshop overview & quick-start guide
├── Student-Guide/
│   ├── IPv4-Addressing-and-Connectivity-Guide.md      # IPv4 subnetting, gateways, DNS & verification
│   ├── Physical-vs-Simulated-Networking.md            # Comparing Cisco Packet Tracer vs. real hardware
│   ├── Packet-Tracer-Guide.md                         # Step-by-step Cisco Packet Tracer lab instructions
│   ├── Physical-Network-Lab-Guide.md                  # Physical switch/router/host cabling & config guide
│   └── Troubleshooting-Challenge.md                   # Fault diagnosis scenarios & rules
├── Worksheets/
│   ├── Topology-Design-Worksheet.md                   # Logical/physical diagram & port mapping sheet
│   ├── IP-Addressing-Worksheet.md                     # Device-by-device IPv4 allocation table
│   ├── Connectivity-Test-Worksheet.md                 # End-to-end ping, gateway, DNS & HTTP test log
│   ├── Environment-Comparison-Worksheet.md            # Simulated vs. physical behavior comparison matrix
│   └── Incident-Report-Template.md                    # Troubleshooting challenge incident report
└── Assets/
    └── Small-Business-Network.pkt                     # Cisco Packet Tracer starter/reference lab file
```

*(Instructor solutions, fault-injection procedures, server setup steps, and grading rubric are located in `Teacher-Resources/Workshop-3-Build-and-Configure-Network/`.)*

---

## 4. Prerequisites & Lab Equipment
* **Software:** Cisco Packet Tracer (installed on student workstations) and Ubuntu Desktop VM / lab hosts with `iproute2` (`ip`), `iputils-ping`, `dnsutils` (`dig`/`nslookup`), and `curl`.
* **Physical Lab Hardware (per team):** Managed/unmanaged Ethernet switch, router or gateway appliance, straight-through Cat5e/Cat6 patch cables, and 2–3 wired client/server endpoints.
* **Shared Standards:** Review the [Lab Safety & Rules](../../00-Shared-Resources/Safety-and-Lab-Rules.md) before handling physical cables, power strips, or rack equipment.
