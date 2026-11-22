# Incident Cards — Workshop 1: IT Troubleshooting Challenge

*Practical Approaches to IT Projects and Problem-Solving* | **Alijó IT Workshops**

> **Instructions:** Your instructor will assign three or four incident cards to your team during the main incident-solving round[cite: 1]. Follow the 7-step troubleshooting methodology for each card, complete one [`Incident-Log.md`](../Worksheets/Incident-Log.md) per incident, and obtain instructor approval before making system-level changes.

---

## INCIDENT 01 – INCORRECT IP CONFIGURATION

**Reported symptoms:**  
A workstation cannot reach other devices on the local network. The network icon may show a connection, but the assigned IPv4 configuration appears incorrect or incomplete.

**Your tasks:**
1. Inspect interfaces and IP settings.
2. Check the routing table.
3. Compare the configuration with the lab network information supplied by the teacher.
4. Identify the incorrect or missing setting.
5. Apply the approved correction or request a VM network reset.
6. Verify local connectivity and record the evidence.

**Suggested diagnostic commands:**
```bash
ip address
ip route
ping -c 4 <LAB_GATEWAY>
