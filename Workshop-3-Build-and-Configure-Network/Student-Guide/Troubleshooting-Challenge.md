# Network Troubleshooting Challenge
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## 1. Challenge Overview & Rules
Your team will receive **two injected network fault scenarios** (one in Cisco Packet Tracer and one on the physical lab network / Ubuntu host) prepared by your instructor. Your mission is to systematically isolate each root cause, restore full end-to-end connectivity, and document your findings in `Worksheets/Incident-Report-Template.md`.

### Ground Rules
1. **Bottom-Up Discipline:** Always test from Layer 1 (Link/Cable) → Layer 2/3 (IP/Subnet/Gateway) → Layer 3 (Routing) → Layer 7 (DNS/HTTP).
2. **One Change at a Time:** Never modify multiple IP addresses, router interfaces, or firewall rules simultaneously.
3. **No Brute-Force Shortcuts:** Do **not** delete and rebuild entire devices, disable host firewalls (`ufw disable`), or reset the whole simulation to bypass diagnosis.
4. **Evidence Required:** Record the exact broken output and the exact post-fix verification output in your Incident Report.

---

## 2. Diagnostic Decision Matrix (Layer 1 to Layer 7)

| Diagnostic Check | Command / Action | If It Fails, Check... |
| :--- | :--- | :--- |
| **1. Physical Link** | `ip -br link` / Check switch LEDs | Unplugged or damaged patch cable, wrong switch port, or router interface administratively `DOWN` (`shutdown`). |
| **2. Local IP & Mask** | `ip -br -4 addr` / `ipconfig /all` | APIPA address (`169.254.x.x` = DHCP failed), wrong subnet mask (`/16` vs `/24`), or duplicate IP conflict. |
| **3. Local Gateway** | `ping -c 3 <Gateway_IP>` | Wrong Default Gateway IP on host, gateway outside host's subnet, or router LAN interface down/misaddressed. |
| **4. Remote Subnet** | `ping -c 3 <Remote_Server_IP>` | Missing router interface IP, wrong subnet mask on `R1`, or DHCP relay (`ip helper-address`) missing. |
| **5. DNS Resolution** | `nslookup intranet.alijo.local` / `dig` | Wrong DNS server IP on client, DNS service stopped on `Server-Core`, or typo in the DNS `A` record. |
| **6. Service & Firewall** | `curl -I http://<Server_IP>:<Port>` / `ufw status` | Web service not running, listening on wrong port, or host firewall blocking inbound TCP traffic. |

---

## 3. Challenge Tickets (Assigned by Instructor)

### Ticket A: Packet Tracer Fault Scenario (`Small-Business-Network-Fault.pkt`)
* **Reported Symptom:** *"Users in the Office LAN (`PC1` and `PC2`) report they can no longer open `http://intranet.alijo.local`. `PC2` also lost its automatic IP configuration after rebooting."*
* **Success Criteria:**
  1. `PC2` obtains a valid IPv4 address (`192.168.10.100–149`), Gateway (`192.168.10.1`), and DNS (`192.168.20.10`) via DHCP.
  2. Both `PC1` and `PC2` successfully ping `192.168.20.10`.
  3. `nslookup intranet.alijo.local` resolves to `192.168.20.10`.
  4. `http://intranet.alijo.local` loads in the Packet Tracer Web Browser on both PCs.

### Ticket B: Physical Lab / Ubuntu Host Fault Scenario
* **Reported Symptom:** *"Client Workstation 1 (`192.168.10.21`) has an active green link LED on the switch, yet cannot reach the local intranet service on Server Host (`192.168.10.10:8080`) or resolve internal hostnames."*
* **Success Criteria:**
  1. `ip -br -4 addr` and `ip route` confirm valid subnet and gateway configuration on both hosts.
  2. `ping -c 3 192.168.10.10` succeeds with `0% packet loss`.
  3. `curl -I http://192.168.10.10:8080` returns `HTTP/1.0 200 OK` (or `HTTP/1.1 200 OK`) with `ufw` remaining active.

---

## 4. Deliverable & Time Target
* **Target Time:** 35–40 minutes total for both tickets.
* **Deliverable:** Complete one `Worksheets/Incident-Report-Template.md` documenting the symptoms, root causes, commands/fixes applied, and verification evidence for your assigned tickets.
