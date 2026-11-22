# Cisco Packet Tracer Lab Guide
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## 1. Lab Objective & Target Topology
In this lab phase, you will build and configure a routed small-business network in **Cisco Packet Tracer** (or complete the starter topology in `Assets/Small-Business-Network.pkt`). Your topology connects two IPv4 subnets through a central router (`R1`):
* **LAN A — Office Network (`192.168.10.0/24`):** Switch `SW-Office` (`2960-24TT`), `PC1` (Static IP), `PC2` (DHCP Client), and `Office-Printer` (Static IP).
* **LAN B — Server Network (`192.168.20.0/24`):** Switch `SW-Servers` (`2960-24TT`) and `Server-Core` (Static IP providing DHCP, DNS, and HTTP services).
* **Core Router (`R1` — `1941` or `2911`):** Routes traffic between LAN A (`GigabitEthernet0/0`) and LAN B (`GigabitEthernet0/1`).

---

## 2. Step 1: Physical Cabling & Device Placement
1. Open Cisco Packet Tracer and place the following devices on the workspace (or open `Assets/Small-Business-Network.pkt`):
   * **Router:** 1× `1941` named `R1`
   * **Switches:** 2× `2960-24TT` named `SW-Office` and `SW-Servers`
   * **End Devices:** 2× `PC-PT` (`PC1`, `PC2`), 1× `Printer-PT` (`Office-Printer`), and 1× `Server-PT` (`Server-Core`)
2. Connect all devices using **Copper Straight-Through** cables according to your `Worksheets/Topology-Design-Worksheet.md`:
   * `R1 GigabitEthernet0/0` ↔ `SW-Office GigabitEthernet0/1`
   * `SW-Office FastEthernet0/1` ↔ `PC1 FastEthernet0`
   * `SW-Office FastEthernet0/2` ↔ `PC2 FastEthernet0`
   * `SW-Office FastEthernet0/3` ↔ `Office-Printer FastEthernet0`
   * `R1 GigabitEthernet0/1` ↔ `SW-Servers GigabitEthernet0/1`
   * `SW-Servers FastEthernet0/1` ↔ `Server-Core FastEthernet0`
3. Enable port labels in Packet Tracer (**Options → Preferences → Always Show Port Labels in Logical Workspace**) to verify every port mapping.

---

## 3. Step 2: Configure Router `R1` Interfaces
Click `R1` → **CLI** tab (or **Config** tab) and configure both Ethernet gateways:

```ios
enable
configure terminal
hostname R1

interface GigabitEthernet0/0
 description LAN-A Office Network
 ip address 192.168.10.1 255.255.255.0
 no shutdown
exit

interface GigabitEthernet0/1
 description LAN-B Server Network
 ip address 192.168.20.1 255.255.255.0
 no shutdown
exit

end
write memory
```

Verify that both link triangles turn **green** (wait ~30 seconds for Spanning Tree on the switches or click **Fast Forward Time** `Alt+D`).

---

## 4. Step 3: Configure `Server-Core` (IP, DNS, HTTP & DHCP)
1. **Static IPv4 Configuration** (`Server-Core` → **Desktop → IP Configuration**):
   * **IPv4 Address:** `192.168.20.10`
   * **Subnet Mask:** `255.255.255.0`
   * **Default Gateway:** `192.168.20.1`
   * **DNS Server:** `192.168.20.10`
2. **HTTP Service** (`Services → HTTP`):
   * Ensure **HTTP** is **On** and edit `index.html` to display `"Alijo Small Business Intranet — Online"`.
3. **DNS Service** (`Services → DNS`):
   * Turn **DNS Service** **On**.
   * Add an **A Record**: Name = `intranet.alijo.local`, Address = `192.168.20.10` → Click **Add**.
4. **DHCP Service** (`Services → DHCP`):
   * Create a pool named `OFFICE_LAN_POOL`:
     * **Default Gateway:** `192.168.10.1`
     * **DNS Server:** `192.168.20.10`
     * **Start IP Address:** `192.168.10.100`
     * **Subnet Mask:** `255.255.255.0`
     * **Maximum Number of Users:** `50`
   * Click **Add** and set **Service** to **On**.

---

## 5. Step 4: Configure DHCP Relay on `R1` & End Devices
Because `PC2` (`192.168.10.0/24`) and `Server-Core` (`192.168.20.0/24`) are on different subnets, `R1` must forward DHCP broadcast requests using `ip helper-address`:

```ios
enable
configure terminal
interface GigabitEthernet0/0
 ip helper-address 192.168.20.10
exit
end
write memory
```

Now configure the LAN A endpoints (`Desktop → IP Configuration`):
* **`PC1` (Static):** IP `192.168.10.21`, Mask `255.255.255.0`, Gateway `192.168.10.1`, DNS `192.168.20.10`.
* **`Office-Printer` (Static):** IP `192.168.10.30`, Mask `255.255.255.0`, Gateway `192.168.10.1`, DNS `192.168.20.10`.
* **`PC2` (DHCP):** Select **DHCP** and confirm it automatically receives an IP in `192.168.10.100–149` with Gateway `192.168.10.1` and DNS `192.168.20.10`.

---

## 6. Step 5: Verification & Simulation Mode Inspection
1. On `PC1` and `PC2`, open **Command Prompt** and run:
   * `ping 192.168.10.1` (Gateway check)
   * `ping 192.168.20.10` (Inter-VLAN routing check)
   * `nslookup intranet.alijo.local` (DNS check)
2. Open **Web Browser** on `PC1` and navigate to `http://intranet.alijo.local`.
3. Switch to **Simulation Mode** (`Shift+S`), filter for **ICMP** and **DNS**, and step through a request from `PC1` to `intranet.alijo.local` to observe ARP resolution, MAC rewriting across `R1`, and DNS query/response frames.
4. Save your completed Packet Tracer file as `Small-Business-Network-Completed.pkt` and log all results in `Worksheets/Connectivity-Test-Worksheet.md`.
