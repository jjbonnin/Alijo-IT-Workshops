# Cisco Packet Tracer Environment Build Guide
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

> **Instructor Reference:** Use this step-by-step specification to build the baseline topology (`Small-Business-Network.pkt`) and the faulted troubleshooting scenario (`Small-Business-Network-Fault.pkt`) in Cisco Packet Tracer.

---

## 1. Device Inventory & Naming
Open Cisco Packet Tracer and drag the following **7 devices** onto the workspace. Rename each device's **Display Name** (under **Config → Global → Settings**) to match the exact topology identifiers:

| Role | Packet Tracer Model | Display Name | Network Segment |
| :--- | :--- | :--- | :--- |
| **Core Router** | `1941` | `R1` | Connects LAN A & LAN B |
| **Office Switch** | `2960-24TT` | `SW-Office` | LAN A (`192.168.10.0/24`) |
| **Server Switch** | `2960-24TT` | `SW-Servers` | LAN B (`192.168.20.0/24`) |
| **Core Server** | `Server-PT` | `Server-Core` | LAN B (`192.168.20.0/24`) |
| **Static Workstation** | `PC-PT` | `PC1` | LAN A (`192.168.10.0/24`) |
| **DHCP Workstation** | `PC-PT` | `PC2` | LAN A (`192.168.10.0/24`) |
| **Network Printer** | `Printer-PT` | `Office-Printer` | LAN A (`192.168.10.0/24`) |

---

## 2. Physical Cabling Connections
Use **Copper Straight-Through** cables for all **6 point-to-point connections**:

| Link # | Source Device | Source Port | Destination Device | Destination Port |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `R1` | `GigabitEthernet0/0` | `SW-Office` | `GigabitEthernet0/1` |
| **2** | `R1` | `GigabitEthernet0/1` | `SW-Servers` | `GigabitEthernet0/1` |
| **3** | `SW-Office` | `FastEthernet0/1` | `PC1` | `FastEthernet0` |
| **4** | `SW-Office` | `FastEthernet0/2` | `PC2` | `FastEthernet0` |
| **5** | `SW-Office` | `FastEthernet0/3` | `Office-Printer` | `FastEthernet0` |
| **6** | `SW-Servers` | `FastEthernet0/1` | `Server-Core` | `FastEthernet0` |

* **Verification:** Click **Fast Forward Time** (`Alt+D`) to skip the 30-second Spanning Tree Protocol (STP) port convergence delay. All switch-to-end-device links should turn **green**; router links remain red until configured in Step 3.

---

## 3. Router `R1` Configuration (Cisco IOS CLI)
Open `R1` → **CLI** (answer `no` if prompted for the initial configuration dialog) and apply:

```ios
enable
configure terminal
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
write memory
```

* **Verification:** Run `show ip interface brief` on `R1` and confirm both `GigabitEthernet0/0` (`192.168.10.1`) and `GigabitEthernet0/1` (`192.168.20.1`) show Status `up` and Protocol `up`.

---

## 4. `Server-Core` Configuration

### 4.1 Static IPv4 Settings
Open `Server-Core` → **Desktop → IP Configuration** → select **Static**:
* **IPv4 Address:** `192.168.20.10`
* **Subnet Mask:** `255.255.255.0`
* **Default Gateway:** `192.168.20.1`
* **DNS Server:** `192.168.20.10`

### 4.2 DHCP Service (`OFFICE_LAN_POOL`)
Open `Server-Core` → **Services → DHCP**:
1. Select `FastEthernet0` and switch **Service** to **On**.
2. Create/save the pool with these exact parameters:
   * **Pool Name:** `OFFICE_LAN_POOL`
   * **Default Gateway:** `192.168.10.1`
   * **DNS Server:** `192.168.20.10`
   * **Start IP Address:** `192.168.10.100`
   * **Subnet Mask:** `255.255.255.0`
   * **Maximum Number of Users:** `50` *(leases `.100` through `.149`)*

### 4.3 DNS Service
Open `Server-Core` → **Services → DNS**:
1. Switch **DNS Service** to **On**.
2. Add the internal intranet record and click **Add**:
   * **Name:** `intranet.alijo.local`
   * **Type:** `A Record`
   * **Address:** `192.168.20.10`

### 4.4 HTTP Service
Open `Server-Core` → **Services → HTTP**:
1. Ensure both **HTTP** and **HTTPS** are set to **On**.
2. Click **(edit)** next to `index.html`, customize the HTML header (e.g., `<h1>Alijo Small Business Intranet</h1>`), and click **Save**.

---

## 5. End-Device Configuration (`LAN A`)

### 5.1 `PC1` (Static Workstation)
Open `PC1` → **Desktop → IP Configuration** → **Static**:
* **IPv4 Address:** `192.168.10.21`
* **Subnet Mask:** `255.255.255.0`
* **Default Gateway:** `192.168.10.1`
* **DNS Server:** `192.168.20.10`

### 5.2 `Office-Printer` (Static Network Printer)
1. Open `Office-Printer` → **Config → Global → Settings**:
   * **Gateway:** `192.168.10.1`
   * **DNS Server:** `192.168.20.10`
2. Open **Config → Interface → FastEthernet0** → **Static**:
   * **IPv4 Address:** `192.168.10.30`
   * **Subnet Mask:** `255.255.255.0`

### 5.3 `PC2` (Dynamic DHCP Workstation)
Open `PC2` → **Desktop → IP Configuration** → select **DHCP**.
* **Verification:** Confirm `DHCP request successful` and verify `PC2` receives `192.168.10.100`, mask `255.255.255.0`, gateway `192.168.10.1`, and DNS `192.168.20.10`.

---

## 6. End-to-End Validation & Exporting `.pkt` Files

### 6.1 Validation Checklist
From `PC2` → **Desktop → Command Prompt**, verify:
```text
ping 192.168.10.1
ping 192.168.20.10
nslookup intranet.alijo.local
```
From `PC2` → **Desktop → Web Browser**, navigate to `http://intranet.alijo.local` and verify the intranet page renders.

### 6.2 Exporting Baseline & Fault Scenarios
1. **Baseline Topology (`Small-Business-Network.pkt`):**
   * Save the verified file via **File → Save As...** into `Workshop-3-Build-and-Configure-Network/Assets/Small-Business-Network.pkt` (optionally strip `R1` and PC IP configs if distributing as an unconfigured starter template).
2. **Troubleshooting Challenge File (`Small-Business-Network-Fault.pkt`):**
   * From the working topology, inject both Ticket A faults and save via **File → Save As...** into `Teacher-Resources/Workshop-3-Build-and-Configure-Network/Solutions-and-Setup/Small-Business-Network-Fault.pkt`:
     * **Fault 1 (DHCP Relay Removed):** On `R1`, enter `interface GigabitEthernet0/0`, run `no ip helper-address 192.168.20.10`, and save with `write memory`. On `PC2`, toggle IP Configuration from `DHCP` → `Static` → `DHCP` so it falls back to an APIPA address (`169.254.x.x`).
     * **Fault 2 (DNS Record Typo):** On `Server-Core` → **Services → DNS**, edit `intranet.alijo.local` to point to `192.168.20.100` instead of `192.168.20.10` and click **Save**.
