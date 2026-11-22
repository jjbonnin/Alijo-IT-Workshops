# IPv4 Addressing Plan Worksheet
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## Team Information
* **Team Name / Number:** ________________________________________
* **Team Members:** ____________________________________________
* **Date:** ____________________________________________________

---

## 1. Subnet Allocation Summary
Complete the subnet breakdown for both networks before assigning individual host IP addresses:

| Network Name | Network Address / CIDR | Subnet Mask | First Usable Host IP | Last Usable Host IP | Broadcast Address | Default Gateway IP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **LAN A (Office Network)** | `192.168.10.0/24` | | | | | |
| **LAN B (Server Network)** | `192.168.20.0/24` | | | | | |

---

## 2. Device-by-Device IPv4 Assignment Table
Fill in the exact addressing details for every device in your topology (confirm zero duplicate IPs and no overlap with the DHCP pool):

| Device Name | Interface | Assignment Method (`Static` / `DHCP`) | IPv4 Address | Subnet Mask | Default Gateway | DNS Server |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `R1` | `GigabitEthernet0/0` | `Static` | `192.168.10.1` | `255.255.255.0` | `N/A (Router)` | `N/A` |
| `R1` | `GigabitEthernet0/1` | `Static` | `192.168.20.1` | `255.255.255.0` | `N/A (Router)` | `N/A` |
| `Server-Core` | `FastEthernet0` / NIC | `Static` | | | | |
| `PC1` | `FastEthernet0` / NIC | `Static` | | | | |
| `Office-Printer` | `FastEthernet0` | `Static` | | | | |
| `PC2` | `FastEthernet0` / NIC | `DHCP` (Record leased IP) | | | | |

---

## 3. DHCP Scope & Reservation Plan (`OFFICE_LAN_POOL`)
Document the DHCP pool parameters configured on `Server-Core`:
* **Pool Name:** `OFFICE_LAN_POOL`
* **Start IPv4 Address:** `192.168.10.100`
* **End IPv4 Address (Calculated from Max Users = 50):** ________________________
* **Subnet Mask:** `255.255.255.0`
* **Default Gateway Option (`Option 003`):** ________________________
* **DNS Server Option (`Option 006`):** ________________________
* **Excluded / Reserved Static Range:** `192.168.10.1` – `192.168.10.99`

---

## 4. Pre-Flight Validation Checklist
Before applying configurations to your devices, verify all four items:
- [ ] Every static IPv4 address is unique across the entire topology.
- [ ] Every host's Default Gateway belongs to the exact same subnet as the host's own IPv4 address.
- [ ] No static IP falls inside the DHCP dynamic lease range (`192.168.10.100`–`192.168.10.149`).
- [ ] Network addresses (`.0`) and broadcast addresses (`.255`) are not assigned to any interface.
