# Physical Network Lab Guide
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## 1. Lab Objective & Hardware Setup
In this phase, you replicate the core connectivity of your simulated topology using real networking hardware and Ubuntu Linux endpoints. Depending on available bench equipment, your team will build either:
* **Option A (Two-Subnet Routed Lab):** 1 router/gateway with two Ethernet interfaces, 2 switches, and 2–3 Ubuntu/client hosts (`192.168.10.0/24` and `192.168.20.0/24`).
* **Option B (Single-Subnet Switch + Gateway Lab):** 1 Ethernet switch connected to the lab gateway (`192.168.10.1/24`), 1 Ubuntu Server (`192.168.10.10`), and 1–2 Ubuntu Client workstations (`192.168.10.21`, DHCP client).

> **Safety First:** Inspect all power cords and RJ45 connectors before plugging in equipment. Never daisy-chain power strips or unplug shared classroom infrastructure cables.

---

## 2. Step 1: Physical Inspection & Layer 1 Cabling
1. **Inspect Patch Cables:** Check that RJ45 locking tabs are intact, wire pairs are properly crimped inside the jack, and cable jackets are undamaged.
2. **Connect Hardware:**
   * Connect **Switch Port 1** to the **Router / Gateway LAN port** using a straight-through Cat5e/Cat6 patch cable.
   * Connect **Server Host** to **Switch Port 2**.
   * Connect **Client Workstation(s)** to **Switch Ports 3 & 4**.
3. **Verify Link LEDs:** Confirm solid or blinking green/amber link LEDs on both the switch ports and each host NIC.
4. **Verify OS Link Detection (Ubuntu):**
   ```bash
   ip -br link
   ```
   Confirm your wired interface (e.g., `enp3s0` or `ens33`) shows state **`UP`**. If it shows `NO-CARRIER`, check the cable seating and switch port power.

---

## 3. Step 2: Configure Static IPv4 Addressing on Ubuntu Hosts
Record your exact interface name (`IFACE`) from `ip -br link`, then assign your team's static IP address cleanly.

### On the Local Server Host (`192.168.10.10/24` or `192.168.20.10/24`)
Using `nmcli` (NetworkManager) or temporary `ip` commands (ask your instructor which method is preferred for your bench):

```bash
# Example using temporary ip commands (non-persistent across reboots)
sudo ip addr flush dev <IFACE>
sudo ip addr add 192.168.10.10/24 dev <IFACE>
sudo ip link set <IFACE> up
sudo ip route add default via 192.168.10.1
```

### On Client Workstation 1 (`192.168.10.21/24`)
```bash
sudo ip addr flush dev <IFACE>
sudo ip addr add 192.168.10.21/24 dev <IFACE>
sudo ip link set <IFACE> up
sudo ip route add default via 192.168.10.1
```

Verify IP and routing table on each machine:
```bash
ip -br -4 addr
ip route
```

---

## 4. Step 3: Start a Local HTTP & DNS Test Service on the Server Host
On the designated **Server Host** (`192.168.10.10`), serve a simple intranet page and verify firewall access:

```bash
mkdir -p ~/alijo-intranet
echo "<h1>Alijo Physical Lab Intranet — Online</h1>" > ~/alijo-intranet/index.html
python3 -m http.server 8080 --directory ~/alijo-intranet &
```

If `ufw` is active on the server host, allow local subnet traffic to port `8080` (never disable the firewall):
```bash
sudo ufw status
sudo ufw allow from 192.168.10.0/24 to any port 8080 proto tcp
```

*(If your instructor enabled `dnsmasq` on the server host, test local DNS resolution; otherwise, map `192.168.10.10 intranet.alijo.local` or query the lab DNS server as instructed.)*

---

## 5. Step 4: End-to-End Physical Verification
From **Client Workstation 1** (`192.168.10.21`), execute the following verification tests in order and record the exact results in `Worksheets/Connectivity-Test-Worksheet.md`:

```bash
# 1. Local TCP/IP stack
ping -c 3 127.0.0.1

# 2. Default Gateway / Router
ping -c 3 192.168.10.1

# 3. Server Host IP connectivity
ping -c 3 192.168.10.10

# 4. Application HTTP connectivity
curl -i [http://192.168.10.10:8080](http://192.168.10.10:8080)
```

---

## 6. Step 5: Cleanup & Bench Reset
Before moving to the Troubleshooting Challenge:
1. Stop any background test HTTP server (`pkill -f "http.server 8080"`).
2. Restore original classroom DHCP/NetworkManager settings on all Ubuntu workstations (`sudo nmcli networking off && sudo nmcli networking on` or reboot/restore VM snapshot).
3. Coil patch cables neatly and leave switches/routers in their baseline configuration.
