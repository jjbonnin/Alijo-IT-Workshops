# 03 — Network Infrastructure & Connectivity Fundamentals
**Alijó IT Workshops | Reference Module**

---

## 1. Module Overview
This module serves as the core technical reference for designing, configuring, and verifying small-business IPv4 networks across both simulated environments (**Cisco Packet Tracer**) and **physical Ethernet lab hardware**. It directly supports **Workshop 3: Build and Configure a Network**.

---

## 2. OSI & TCP/IP Layer Quick-Reference for Engineers

| Layer | TCP/IP Model | Key Protocols & Standards | Primary Devices | Common Verification Tools |
| :--- | :--- | :--- | :--- | :--- |
| **Layer 7 (Application)** | Application | HTTP/HTTPS, DNS, DHCP, SSH | Servers, Clients | `curl`, `nslookup`, `dig`, Web Browser |
| **Layer 4 (Transport)** | Transport | TCP (reliable), UDP (connectionless) | Host Firewalls (`ufw`) | `ss -tulpn`, `nc -zv`, `ufw status` |
| **Layer 3 (Network)** | Internet | IPv4, ICMP, ARP, Static Routing | Routers (`R1`), L3 Switches | `ip -br -4 addr`, `ip route`, `ping`, `traceroute` |
| **Layer 2 (Data Link)** | Network Access | Ethernet (802.3), MAC, VLANs, STP | Switches (`SW-Office`) | `ip neigh`, `show mac address-table` |
| **Layer 1 (Physical)** | Network Access | Cat5e/Cat6 UTP, RJ45, Fiber, Link LEDs | NICs, Patch Panels, Cables | `ip -br link`, Physical Link LEDs |

---

## 3. IPv4 Subnetting & Addressing Cheatsheet (`/24` Standard)
* **Network Address (`.0`):** Identifies the subnet itself (cannot be assigned to a host).
* **First Usable Host (`.1`):** Standard convention for the **Default Gateway** router interface.
* **Reserved Infrastructure Range (`.2` – `.99`):** Recommended for static servers, switches, access points, and network printers.
* **Dynamic DHCP Pool (`.100` – `.249`):** Leased automatically to end-user workstations and laptops.
* **Broadcast Address (`.255`):** Delivers frames/packets to all hosts on the local subnet.

---

## 4. Essential Cross-Platform Network Commands

### Linux (Ubuntu / Debian)
```bash
ip -br link                      # Check physical link state (UP/DOWN)
ip -br -4 addr                   # View assigned IPv4 addresses and CIDR masks
ip route                         # Inspect default gateway and routing table
ping -c 4 192.168.10.1           # Test Layer 3 reachability
dig @192.168.20.10 intranet.alijo.local +short   # Query specific DNS server
curl -I [http://192.168.20.10](http://192.168.20.10)     # Verify HTTP response headers
```

### Cisco IOS (Routers & Switches)
```ios
show ip interface brief          ! Verify interface IP addresses and up/up status
show ip route                    ! Inspect connected and static routes
show running-config              ! Review active device configuration
copy running-config startup-config ! Persist changes across reboots
```

---

## 5. Related Workshop Materials
* **Hands-On Workshop:** `../Workshop-3-Build-and-Configure-Network/`
* **Instructor Guide & Solutions:** `../Teacher-Resources/Workshop-3-Build-and-Configure-Network/`
