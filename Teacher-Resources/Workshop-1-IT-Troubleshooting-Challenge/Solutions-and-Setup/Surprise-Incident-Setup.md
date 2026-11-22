# Surprise Incident Setup (Incident 06)

**Workshop 1: IT Troubleshooting Challenge | Alijó IT Workshops**

> **Confidentiality Notice:** This document is intended exclusively for instructors. Do not share with students.

## 1. Overview

The "Surprise Incident" is designed to test the students' ability to apply the 7-step troubleshooting methodology under time pressure and without a detailed pre-briefing.

**Scenario:** A VM that was working earlier can no longer reach the lab gateway or an external IP address. The team has inherited the machine after a configuration change. The cause is not stated.

**Timing:** This incident should be released around **minute 115** of the workshop. Do not provide additional hints unless a team is completely stuck and safety is a concern.

## 2. Preparation & Fault Injection

Before injecting the fault, ensure the students have saved their work for Incidents 01-05. You can inject this fault directly into their running VM or have them switch to a secondary VM prepared in advance.

### The Fault: Default Gateway Removal

To simulate a sudden loss of external connectivity while maintaining local link status, delete the default route.

1. Access the student's Ubuntu VM (either by asking them to step away for a moment, or via remote SSH if configured in your lab).

2. Run the following command to delete the default gateway:

   ```bash
   sudo ip route del default
   ```

3. *(Optional Alternative)* If you prefer to simulate a completely disabled network adapter instead of just a routing issue:

   ```bash
   sudo nmcli con down "Wired connection 1"
   ```

## 3. Expected Student Actions

Students should systematically diagnose the issue layer by layer, rather than making random changes:

1. **Verify symptoms:** Run `ping 1.1.1.1` or `ping 8.8.8.8` and receive a `Network is unreachable` error.

2. **Check interfaces:** Run `ip address`. They will see that the interface still has an IP address (if the route was deleted).

3. **Check routing:** Run `ip route`. They should notice that the line starting with `default via ...` is completely missing compared to the baseline notes they took at the start of the workshop.

4. **Form Hypothesis:** The default gateway configuration was removed or the routing table is missing its default path.

## 4. Recovery & Verification

Students can resolve the incident by restoring the network connection profile, which will pull the correct route back into the table.

**Approved Student Fixes:**

* **Option A (Restart NetworkManager connection - Recommended):**

  ```bash
  sudo nmcli con up "Wired connection 1"
  ```
  *(This is the most common and robust fix as it cleanly reapplies the DHCP or static profile).*

* **Option B (Manually add the route):**

  ```bash
  sudo ip route add default via <GATEWAY_IP>
  ```

**Final Verification:**
Students must run `ping -c 4 <GATEWAY_IP>` followed by `ping -c 4 1.1.1.1` to prove connectivity is restored. They must then document the exact symptoms, the missing route, and the fix in their Final Report.
