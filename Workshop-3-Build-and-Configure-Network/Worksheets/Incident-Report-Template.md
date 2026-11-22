# Network Troubleshooting Incident Report
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## Incident Metadata
* **Team Name / Number:** ________________________________________
* **Team Members & Roles:** ____________________________________
* **Date:** ____________________________________________________
* **Environment(s) Tested:** [ ] Cisco Packet Tracer (`Ticket A`)  [ ] Physical Lab / Ubuntu (`Ticket B`)

---

## 1. Ticket A — Cisco Packet Tracer Fault Analysis

### 1.1 Reported Symptoms & Scope
* **Initial User Report:** _______________________________________________________
* **Affected Devices / Subnets:** ________________________________________________

### 1.2 Layer-by-Layer Diagnostic Findings
| Layer | Diagnostic Test Performed | Observed Output (Before Fix) | Status (`OK` / `FAULT`) |
| :--- | :--- | :--- | :--- |
| **Layer 1 (Link)** | | | |
| **Layer 2/3 (Local IP/DHCP)** | | | |
| **Layer 3 (Gateway & Routing)** | | | |
| **Layer 7 (DNS & HTTP)** | | | |

### 1.3 Root Cause(s) Identified
1. **Root Cause 1:** ___________________________________________________________
2. **Root Cause 2 (if applicable):** _____________________________________________

### 1.4 Remediation Steps Applied
List the exact CLI commands or configuration changes applied to resolve Ticket A:
```ios
! Paste exact Cisco IOS / device configuration fixes here
```

### 1.5 Post-Fix Verification Evidence
Paste the output of `ipconfig /all`, `ping`, `nslookup`, and HTTP browser checks confirming full recovery:
```text
# Paste verification command outputs here
```

---

## 2. Ticket B — Physical Lab / Ubuntu Host Fault Analysis

### 2.1 Reported Symptoms & Scope
* **Initial User Report:** _______________________________________________________
* **Affected Hosts & Interfaces:** _______________________________________________

### 2.2 Layer-by-Layer Diagnostic Findings
| Layer | Diagnostic Command Executed | Observed Output (Before Fix) | Status (`OK` / `FAULT`) |
| :--- | :--- | :--- | :--- |
| **Layer 1 (`ip -br link`)** | | | |
| **Layer 3 (`ip -br -4 addr` / `ip route`)** | | | |
| **Layer 4 (`ufw status` / `ss -tulpn`)** | | | |
| **Layer 7 (`dig` / `curl`)** | | | |

### 2.3 Root Cause(s) Identified
1. **Root Cause 1:** ___________________________________________________________
2. **Root Cause 2 (if applicable):** _____________________________________________

### 2.4 Remediation Steps Applied
List the exact Linux commands applied (confirming `ufw` remained enabled if firewall rules were adjusted):
```bash
# Paste exact remediation commands here
```

### 2.5 Post-Fix Verification Evidence
Paste the exact post-fix outputs (`ping`, `curl -I`, `ufw status`):
```text
# Paste verification outputs here
```

---

## 3. Preventive Recommendations
1. **Configuration / Documentation Improvement:** _______________________________
2. **Verification Habit for Future Deployments:** ________________________________
