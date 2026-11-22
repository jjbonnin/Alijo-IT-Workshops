# Fault Injection and Recovery Guide (Instructor Key)
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## 1. Overview of Troubleshooting Challenge Tickets
During Phase 3 (`Troubleshooting-Challenge.md`), instructors deploy two controlled faults—one in Cisco Packet Tracer (**Ticket A**) and one on the Ubuntu physical lab server/client (**Ticket B**). Both faults are deterministic, reversible, and directly test the student Bottom-Up methodology.

---

## 2. Ticket A: Cisco Packet Tracer Fault (`Small-Business-Network-Fault.pkt`)

### 2.1 How to Prepare the Faulted `.pkt` File Before Class
Starting from a working `Small-Business-Network-Completed.pkt` file, introduce these **two layered faults** and save as `Small-Business-Network-Fault.pkt`:
1. **Fault A1 (Missing DHCP Relay):** On `R1` (`GigabitEthernet0/0`), remove the DHCP helper command:
   ```ios
   enable
   configure terminal
   interface GigabitEthernet0/0
    no ip helper-address 192.168.20.10
   end
   write memory
   ```
   *(Then renew DHCP on `PC2` so it falls back to an APIPA `169.254.x.x` address.)*
2. **Fault A2 (DNS Record Typo):** On `Server-Core` → **Services → DNS**, edit the `A` record for `intranet.alijo.local` to point to the wrong IP (`192.168.20.100` instead of `192.168.20.10`).

### 2.2 Expected Student Diagnosis & Solution Key
* **Symptom 1 (`PC2` loses IP):** `ipconfig /all` shows `169.254.x.x`. Ping to `192.168.10.1` fails, while `PC1` (`192.168.10.21`) still pings `192.168.10.1` and `192.168.20.10` normally. This isolates the issue to DHCP forwarding across `R1`.
  * **Fix A1:** Add `ip helper-address 192.168.20.10` under `interface GigabitEthernet0/0` on `R1` and toggle DHCP on `PC2`.
* **Symptom 2 (`PC1` cannot open `http://intranet.alijo.local`):** `ping 192.168.20.10` succeeds, and `http://192.168.20.10` loads in the browser, but `nslookup intranet.alijo.local` returns `192.168.20.100`. This isolates the issue to DNS resolution.
  * **Fix A2:** Update the `intranet.alijo.local` `A` record on `Server-Core` to `192.168.20.10`.

---

## 3. Ticket B: Physical Lab / Ubuntu Host Fault

### 3.1 How to Inject the Fault on the Ubuntu Server Host (`192.168.10.10`)
Ensure the HTTP server is running on port `8080`, then inject a firewall block on port `8080` (simulating an incomplete service deployment) and misconfigure `/etc/hosts` on Client Workstation 1 (`192.168.10.21`):

**On Server Host (`192.168.10.10`):**
```bash
sudo ufw delete allow from 192.168.10.0/24 to any port 8080 proto tcp 2>/dev/null || true
sudo ufw deny in on any to any port 8080 proto tcp
sudo ufw --force enable
```

**On Client Workstation 1 (`192.168.10.21`):**
```bash
# Inject a wrong IP mapping for intranet.alijo.local
sudo sed -i '/intranet.alijo.local/d' /etc/hosts
echo "192.168.10.99 intranet.alijo.local" | sudo tee -a /etc/hosts
```

### 3.2 Expected Student Diagnosis & Solution Key
1. **Layer 1 & 3 Check:** `ip -br link`, `ip -br -4 addr`, and `ping -c 3 192.168.10.10` all succeed (`0% packet loss`), proving physical cabling and IP routing are healthy.
2. **Layer 4/7 HTTP Check:** `curl -I http://192.168.10.10:8080` hangs/times out. Checking `sudo ufw status numbered` on the server reveals the explicit `DENY IN` rule on `8080/tcp`.
   * **Fix B1 (Server Host):** Remove the deny rule and allow subnet traffic without disabling `ufw`:
```bash
sudo ufw delete deny in on any to any port 8080 proto tcp
sudo ufw allow from 192.168.10.0/24 to any port 8080 proto tcp
```
3. **Layer 7 Hostname Check:** `ping intranet.alijo.local` tries to reach `192.168.10.99`. Inspecting `/etc/hosts` (or `getent hosts intranet.alijo.local`) reveals the stale/wrong IP mapping.
   * **Fix B2 (Client Workstation 1):** Update `/etc/hosts` (or `dnsmasq`) so `intranet.alijo.local` points to `192.168.10.10`.

---

## 4. Full Recovery & Bench Reset Commands
Run after grading Ticket B to return both machines to a clean state:

```bash
# On Server Host
pkill -f "http.server 8080" || true
sudo ufw --force reset

# On Client Workstation 1
sudo sed -i '/intranet.alijo.local/d' /etc/hosts
```
