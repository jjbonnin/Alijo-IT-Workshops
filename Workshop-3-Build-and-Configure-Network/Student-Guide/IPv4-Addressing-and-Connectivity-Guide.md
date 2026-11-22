# IPv4 Addressing and Connectivity Guide
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## 1. Anatomy of an IPv4 Host Configuration
For any device (PC, server, printer, or router interface) to communicate across a local network and beyond, four parameters must be configured consistently:

| Parameter | Purpose | Example (`192.168.10.0/24`) |
| :--- | :--- | :--- |
| **IPv4 Address** | Unique 32-bit host identifier on the local subnet. | `192.168.10.21` |
| **Subnet Mask** | Defines which bits identify the **Network** vs. the **Host**. | `255.255.255.0` (`/24`) |
| **Default Gateway** | IP address of the local router interface used to reach external subnets. | `192.168.10.1` |
| **DNS Server** | IP address of the server that resolves hostnames (e.g., `intranet.alijo.local`) to IPs. | `192.168.10.10` |

---

## 2. Private IPv4 Ranges (RFC 1918) & Subnet Calculations
Internal business and lab networks use private IPv4 blocks:
* **Class A:** `10.0.0.0/8` (`10.0.0.0` – `10.255.255.255`)
* **Class B:** `172.16.0.0/12` (`172.16.0.0` – `172.31.255.255`)
* **Class C:** `192.168.0.0/16` (`192.168.0.0` – `192.168.255.255`)

### Quick CIDR Reference for Small Business LANs

| CIDR | Subnet Mask | Total Addresses | Usable Host IPs | Typical Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **`/24`** | `255.255.255.0` | 256 | **254** (`.1` – `.254`) | Standard office LAN or VLAN |
| **`/25`** | `255.255.255.128` | 128 | **126** | Medium department subnet |
| **`/26`** | `255.255.255.192` | 64 | **62** | Small office / server segment |
| **`/27`** | `255.255.255.224` | 32 | **30** | Management or printer subnet |
| **`/30`** | `255.255.255.252` | 4 | **2** | Point-to-point router-to-router link |

> **Golden Rules of IPv4 Assignment:**
> 1. Never assign the **Network Address** (first IP, e.g., `.0` in `/24`) or **Broadcast Address** (last IP, e.g., `.255` in `/24`) to a host.
> 2. Never assign the same IP address to two devices (**IP Conflict**).
> 3. The **Default Gateway** must reside inside the **exact same subnet** as the host.
> 4. Keep static infrastructure (routers, switches, servers, printers) in a dedicated reserved block (e.g., `.1`–`.50`) separate from the DHCP pool (e.g., `.100`–`.200`).

---

## 3. Standard Small-Business Reference Addressing Plan
Throughout Workshop 3, our reference small business topology uses two routed subnets connected via a central router (`R1`):
* **LAN A (Office Workstations & Printers):** `192.168.10.0/24` — Gateway `192.168.10.1`
* **LAN B (Local Services — DHCP / DNS / Web Server):** `192.168.20.0/24` — Gateway `192.168.20.1`

---

## 4. Layer-by-Layer Connectivity Verification Commands

Run tests strictly from **Bottom to Top** (Layer 1 → Layer 7):

| Step | Layer | What You Are Testing | Linux / Ubuntu Command | Packet Tracer / Windows Equivalent |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Layer 1 (Link)** | Cable connected & interface `UP` | `ip -br link` | Green link triangles / `ipconfig` |
| **2** | **Layer 2/3 (Local IP)** | Correct IP & mask assigned | `ip -br -4 addr` | `ipconfig /all` |
| **3** | **Layer 3 (Loopback)** | Local TCP/IP stack healthy | `ping -c 3 127.0.0.1` | `ping 127.0.0.1` |
| **4** | **Layer 3 (Gateway)** | Local LAN switching & router reachability | `ping -c 3 192.168.10.1` | `ping 192.168.10.1` |
| **5** | **Layer 3 (Routing)** | Inter-VLAN / remote subnet routing | `ping -c 3 192.168.20.10` | `tracert 192.168.20.10` |
| **6** | **Layer 7 (DNS)** | Hostname-to-IP resolution | `dig @192.168.20.10 intranet.alijo.local` | `nslookup intranet.alijo.local` |
| **7** | **Layer 7 (HTTP)** | Application service response | `curl -I http://intranet.alijo.local` | Packet Tracer Web Browser |

---

## 5. Common IPv4 Misconfigurations & Symptoms
* **Wrong Subnet Mask (e.g., `/16` instead of `/24`):** Host believes remote devices are on its local LAN, sends ARP requests instead of forwarding to the gateway, and fails to reach other subnets.
* **Missing or Wrong Default Gateway:** Host can ping devices on its own switch (`192.168.10.x`), but cannot reach `192.168.20.x`.
* **Duplicate IP Address:** Intermittent packet loss and ARP warnings (`duplicate use of IP detected`).
* **DHCP Pool Overlapping Static IPs:** Newly booted clients receive an IP already assigned to a server or printer.
