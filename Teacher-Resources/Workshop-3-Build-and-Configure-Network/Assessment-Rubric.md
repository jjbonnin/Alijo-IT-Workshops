# Assessment Rubric — Workshop 3: Build and Configure a Network
**Practical Approaches to IT Projects and Problem-Solving | Alijó IT Workshops**

---

## 1. Grading Overview (100 Points Total)
Teams are evaluated across five practical competencies combining design rigor, simulated and physical implementation, comparative analysis, and structured troubleshooting.

| Evaluation Area | Weight | Evidence Source |
| :--- | :--- | :--- |
| **1. Topology Design & IPv4 Addressing Plan** | **20 pts** | `Topology-Design-Worksheet.md` & `IP-Addressing-Worksheet.md` |
| **2. Cisco Packet Tracer Build & Verification** | **25 pts** | Completed `.pkt` file & `Connectivity-Test-Worksheet.md` (Part A) |
| **3. Physical Network Lab Execution & Safety** | **20 pts** | Bench inspection & `Connectivity-Test-Worksheet.md` (Part B) |
| **4. Simulated vs. Physical Comparative Analysis** | **15 pts** | `Environment-Comparison-Worksheet.md` |
| **5. Troubleshooting Challenge & Incident Report** | **20 pts** | Live fix verification & `Incident-Report-Template.md` |

---

## 2. Detailed Scoring Criteria

### 1. Topology Design & IPv4 Addressing Plan (20 Points)
* **18–20 pts (Exemplary):** Complete, accurate topology diagram and port mapping table; zero IP conflicts; all gateways match host subnets; DHCP pool (`192.168.10.100–149`) cleanly separated from static infrastructure; pre-flight checklist verified.
* **14–17 pts (Proficient):** Functional IP plan and port map with 1 minor omission (e.g., missing cable type or DHCP end-IP calculation) corrected before build.
* **10–13 pts (Developing):** Multiple IP subnet/gateway mismatches or overlapping DHCP scope requiring instructor intervention.
* **0–9 pts (Incomplete):** Incomplete worksheets or unaddressed network segments.

### 2. Cisco Packet Tracer Build & Verification (25 Points)
* **22–25 pts (Exemplary):** All links green; `R1` routes cleanly between `192.168.10.0/24` and `192.168.20.0/24`; `ip helper-address` configured so `PC2` obtains DHCP dynamically; DNS (`intranet.alijo.local`) and HTTP page load verified from both PCs; Simulation Mode observations accurately recorded.
* **17–21 pts (Proficient):** Inter-VLAN routing and static IPs work, but 1 service (e.g., cross-subnet DHCP relay or DNS record) has a minor configuration gap.
* **11–16 pts (Developing):** Only local single-switch communication works; router interfaces down or misconfigured.
* **0–10 pts (Incomplete):** Topology non-functional or unsubmitted.

### 3. Physical Network Lab Execution & Safety (20 Points)
* **18–20 pts (Exemplary):** Clean physical cabling with verified link LEDs (`ip -br link` `UP`), accurate static IP/gateway configuration on Ubuntu hosts, working HTTP test service (`curl` returns `200 OK`), safe `ufw` rule usage, and full bench cleanup at end of phase.
* **14–17 pts (Proficient):** Physical connectivity and HTTP test achieved with minor CLI syntax help; clean bench reset completed.
* **10–13 pts (Developing):** Struggled with interface identification or routing table setup; partial connectivity only.
* **0–9 pts (Incomplete):** Unsafe cable handling, disabled firewall instead of targeted rule, or incomplete lab.

### 4. Simulated vs. Physical Comparative Analysis (15 Points)
* **14–15 pts (Exemplary):** Identifies 4+ concrete, technically accurate differences across layers (STP delay, `ufw` ICMP blocking, physical cable/NIC link states, real latency variance) with thoughtful engineering reflections.
* **10–13 pts (Proficient):** Identifies 3 valid differences with clear explanations.
* **6–9 pts (Developing):** Generic or superficial comparisons without specific lab evidence.
* **0–5 pts (Incomplete):** Worksheet largely blank.

### 5. Troubleshooting Challenge & Incident Report (20 Points)
* **18–20 pts (Exemplary):** Diagnosed both Ticket A (Packet Tracer) and Ticket B (Physical/Ubuntu) using strict Bottom-Up methodology; isolated exact root causes; restored full connectivity without disabling `ufw` or rebuilding devices; submitted complete `Incident-Report-Template.md` with before/after evidence.
* **14–17 pts (Proficient):** Resolved both tickets with minor hints; incident report documents root causes and final verification.
* **10–13 pts (Developing):** Resolved only one ticket or relied on trial-and-error changes without systematic layer checks.
* **0–9 pts (Incomplete):** Faults unresolved or report lacks diagnostic evidence.
