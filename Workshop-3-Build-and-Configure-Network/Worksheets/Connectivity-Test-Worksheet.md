# Connectivity Test Worksheet
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## Team Information
* **Team Name / Number:** ________________________________________
* **Team Members:** ____________________________________________
* **Date:** ____________________________________________________

---

## 1. Part A — Cisco Packet Tracer Verification Matrix
Execute each test from bottom (Layer 1) to top (Layer 7) and record exact results:

| Test # | Source Device | Target / Destination | Test Command / Tool | Expected Result | Actual Result (`PASS` / `FAIL`) | Observed Output / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | `PC1` | `127.0.0.1` (Loopback) | `ping 127.0.0.1` | 4/4 Replies (`0% loss`) | | |
| **2** | `PC1` | `192.168.10.1` (`R1 Gi0/0`) | `ping 192.168.10.1` | 4/4 Replies (`0% loss`) | | |
| **3** | `PC1` | `192.168.10.30` (`Printer`) | `ping 192.168.10.30` | 4/4 Replies (`0% loss`) | | |
| **4** | `PC1` | `192.168.20.1` (`R1 Gi0/1`) | `ping 192.168.20.1` | 4/4 Replies (`0% loss`) | | |
| **5** | `PC1` | `192.168.20.10` (`Server`) | `ping 192.168.20.10` | 4/4 Replies (`0% loss`) | | |
| **6** | `PC2` | DHCP Server (`Server-Core`) | `ipconfig /all` | IP in `.100–.149`, GW `.10.1` | | |
| **7** | `PC2` | `intranet.alijo.local` (DNS) | `nslookup intranet.alijo.local` | Resolves to `192.168.20.10` | | |
| **8** | `PC2` | `http://intranet.alijo.local` | Web Browser | Displays Intranet Web Page | | |

---

## 2. Part B — Physical Lab Network Verification Matrix
Record the exact command outputs obtained on your physical Ubuntu / lab hosts:

| Test # | Source Host | Target / Destination | Linux CLI Command | Expected Result | Actual Result (`PASS` / `FAIL`) | Observed Output / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Client 1 | Local NIC Link | `ip -br link` | Interface state `UP` | | |
| **2** | Client 1 | Local IPv4 Address | `ip -br -4 addr` | Valid subnet IP assigned | | |
| **3** | Client 1 | Default Gateway | `ping -c 3 <Gateway_IP>` | `3 received, 0% packet loss` | | |
| **4** | Client 1 | Physical Server Host | `ping -c 3 <Server_IP>` | `3 received, 0% packet loss` | | |
| **5** | Client 1 | Local HTTP Service | `curl -I http://<Server_IP>:8080` | `HTTP/1.0 200 OK` | | |

---

## 3. Packet Flow Observation (Simulation Mode)
When running `ping` or `nslookup` from `PC1` (`192.168.10.21`) to `Server-Core` (`192.168.20.10`) in Packet Tracer **Simulation Mode**:
1. **What destination MAC address does `PC1` place on the Ethernet frame when sending a packet to `192.168.20.10`?**  
   *Observed MAC / Device:* ____________________________________________________

2. **How does `R1` modify the Layer 2 and Layer 3 headers as the packet moves from `Gi0/0` to `Gi0/1`?**  
   *Layer 2 (MAC):* ___________________________________________________________  
   *Layer 3 (IPv4):* ___________________________________________________________
