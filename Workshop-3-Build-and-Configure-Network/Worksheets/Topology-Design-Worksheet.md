# Topology Design Worksheet
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## Team Information
* **Team Name / Number:** ________________________________________
* **Team Members:** ____________________________________________
* **Date:** ____________________________________________________

---

## 1. Logical Network Diagram
Draw or paste an ASCII/exported diagram of your small-business network showing both subnets (`192.168.10.0/24` and `192.168.20.0/24`), router interfaces, switches, server, and client endpoints:

```text
[ Example Sketch Area — Update with your exact interfaces and hostnames ]

   (PC1) ----\
   (PC2) -----+--- [ SW-Office ] --- (Gi0/0) [ R1 ] (Gi0/1) --- [ SW-Servers ] --- (Server-Core)
 (Printer) --/     192.168.10.0/24                               192.168.20.0/24
```

---

## 2. Device Inventory & Role Matrix

| Device Name | Device Type / Model | Network Segment | Primary Role / Services Hosted |
| :--- | :--- | :--- | :--- |
| `R1` | | LAN A & LAN B | Inter-VLAN / inter-subnet routing & DHCP relay |
| `SW-Office` | | LAN A (`192.168.10.0/24`) | Layer 2 access switching for office endpoints |
| `SW-Servers` | | LAN B (`192.168.20.0/24`) | Layer 2 access switching for local servers |
| `Server-Core` | | LAN B (`192.168.20.0/24`) | Static IP — DHCP, DNS, HTTP Intranet |
| `PC1` | | LAN A (`192.168.10.0/24`) | Static IP workstation |
| `PC2` | | LAN A (`192.168.10.0/24`) | Dynamic (DHCP) workstation |
| `Office-Printer` | | LAN A (`192.168.10.0/24`) | Static IP network printer |

---

## 3. Physical & Simulated Cabling / Port Mapping Table
Document every point-to-point cable connection before building in Packet Tracer or on the physical bench:

| Link # | Source Device | Source Port | Destination Device | Destination Port | Cable Type (Straight / Crossover) | Verified Link Status (`UP` / Green) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | `R1` | `GigabitEthernet0/0` | `SW-Office` | `GigabitEthernet0/1` | | [ ] Yes |
| **2** | `R1` | `GigabitEthernet0/1` | `SW-Servers` | `GigabitEthernet0/1` | | [ ] Yes |
| **3** | `SW-Office` | `FastEthernet0/1` | `PC1` | `FastEthernet0` | | [ ] Yes |
| **4** | `SW-Office` | `FastEthernet0/2` | `PC2` | `FastEthernet0` | | [ ] Yes |
| **5** | `SW-Office` | `FastEthernet0/3` | `Office-Printer` | `FastEthernet0` | | [ ] Yes |
| **6** | `SW-Servers` | `FastEthernet0/1` | `Server-Core` | `FastEthernet0` | | [ ] Yes |

---

## 4. Design Justification Questions
1. **Why are `Server-Core` and the office workstations placed in separate IPv4 subnets (`192.168.20.0/24` vs. `192.168.10.0/24`)?**  
   *Answer:* ____________________________________________________________________

2. **Why is a straight-through Ethernet cable used between a switch port and a router interface, or between a switch port and a PC?**  
   *Answer:* ____________________________________________________________________
