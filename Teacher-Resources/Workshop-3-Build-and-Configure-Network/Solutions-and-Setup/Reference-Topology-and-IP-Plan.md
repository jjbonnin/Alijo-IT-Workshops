# Reference Topology and IPv4 Addressing Plan (Instructor Answer Key)
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## 1. Reference Logical & Physical Topology

```text
  [ PC1 ] (192.168.10.21) ── Fa0/1 ──┐
  [ PC2 ] (DHCP: .100-.149) ─ Fa0/2 ─┼── [ SW-Office ] (2960-24TT)
  [ Printer ] (192.168.10.30) ─ Fa0/3 ┘        │ Gi0/1 (Straight-Through)
                                               │
                                               ▼ Gi0/0 (192.168.10.1/24)
                                            [ R1 ] (1941 Router)
                                               │ Gi0/1 (192.168.20.1/24)
                                               │
                                               ▼ Gi0/1 (Straight-Through)
                                         [ SW-Servers ] (2960-24TT)
                                               │ Fa0/1
                                               ▼
                                        [ Server-Core ] (192.168.20.10/24)
                                        Services: DHCP, DNS, HTTP
```

---

## 2. Completed Subnet Allocation Key (`Worksheets/IP-Addressing-Worksheet.md`)

| Network Name | Network Address / CIDR | Subnet Mask | First Usable Host IP | Last Usable Host IP | Broadcast Address | Default Gateway IP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **LAN A (Office Network)** | `192.168.10.0/24` | `255.255.255.0` | `192.168.10.1` | `192.168.10.254` | `192.168.10.255` | `192.168.10.1` |
| **LAN B (Server Network)** | `192.168.20.0/24` | `255.255.255.0` | `192.168.20.1` | `192.168.20.254` | `192.168.20.255` | `192.168.20.1` |

---

## 3. Completed Device-by-Device IPv4 Assignment Key

| Device Name | Interface | Method | IPv4 Address | Subnet Mask | Default Gateway | DNS Server |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `R1` | `GigabitEthernet0/0` | `Static` | `192.168.10.1` | `255.255.255.0` | `N/A (Router)` | `N/A` |
| `R1` | `GigabitEthernet0/1` | `Static` | `192.168.20.1` | `255.255.255.0` | `N/A (Router)` | `N/A` |
| `Server-Core` | `FastEthernet0` | `Static` | `192.168.20.10` | `255.255.255.0` | `192.168.20.1` | `192.168.20.10` |
| `PC1` | `FastEthernet0` | `Static` | `192.168.10.21` | `255.255.255.0` | `192.168.10.1` | `192.168.20.10` |
| `Office-Printer` | `FastEthernet0` | `Static` | `192.168.10.30` | `255.255.255.0` | `192.168.10.1` | `192.168.20.10` |
| `PC2` | `FastEthernet0` | `DHCP` | `192.168.10.100` *(first lease)* | `255.255.255.0` | `192.168.10.1` | `192.168.20.10` |

* **DHCP Scope End IP (`Max Users = 50` starting at `.100`):** `192.168.10.149` (`.100` through `.149` inclusive = 50 addresses).

---

## 4. Complete Cisco IOS Running Configuration for `R1`

```ios
hostname R1
!
interface GigabitEthernet0/0
 description LAN-A Office Network
 ip address 192.168.10.1 255.255.255.0
 ip helper-address 192.168.20.10
 no shutdown
!
interface GigabitEthernet0/1
 description LAN-B Server Network
 ip address 192.168.20.1 255.255.255.0
 no shutdown
!
end
```

---

## 5. Key Answer Points for Student Worksheet Questions
1. **Why separate Office and Server subnets?** Isolates broadcast domains, improves security/access control between general user workstations and critical servers, and mirrors real segmented business architecture.
2. **Why Straight-Through cables between Switch–Router and Switch–PC?** Switches are MDI-X devices while routers and PCs are MDI devices (transmitting on pins 1–2 and receiving on pins 3–6), so straight-through wiring aligns TX to RX automatically.
3. **Simulation Mode MAC Header Behavior:** When `PC1` (`192.168.10.21`) pings `192.168.20.10`, the Layer 2 destination MAC is `R1 GigabitEthernet0/0` (the default gateway). `R1` strips the LAN A Ethernet header, rewrites source/destination MACs for LAN B (`R1 Gi0/1` → `Server-Core`), and leaves the Layer 3 source (`192.168.10.21`) and destination (`192.168.20.10`) IPv4 addresses unchanged.
