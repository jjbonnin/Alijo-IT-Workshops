# VMware Workstation / Fusion Lab Virtualization Guide
**04 — System Administration | Alijó IT Workshops**

---

## 1. Purpose
This reference guide explains how to configure virtual network modes, snapshots, and multi-VM lab topologies in **VMware Workstation Pro / Player** or **VMware Fusion** so students and instructors can safely run Ubuntu Server and client virtual machines.

---

## 2. Virtual Network Adapter Modes Compared

| VMware Network Mode | How It Works | Internet Access? | Reachable from Host? | Reachable from Other Physical PCs on LAN? | Best Lab Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NAT (Default)** | VM shares the host's IP via VMware's built-in NAT engine and virtual DHCP server (`vmnet8`). | **Yes** | **Yes** (from host OS) | **No** (isolated behind host NAT) | Single-VM labs needing `apt` internet access without affecting classroom LAN DHCP. |
| **Bridged** | VM connects directly to the physical Ethernet/Wi-Fi switch as an independent node on the classroom network. | **Yes** (via classroom gateway) | **Yes** | **Yes** | Multi-workstation labs where peers or physical switches need to ping/SSH into the VM. |
| **Host-Only** | Creates a private isolated virtual switch (`vmnet1`) shared strictly between the host OS and local VMs. | **No** | **Yes** | **No** | Isolated malware/firewall testing or multi-VM internal subnets without external traffic. |
| **Custom (`VMnet2`–`VMnet19`)** | Dedicated virtual Layer 2 switch connecting only VMs assigned to that specific `VMnet`. | **No** (unless routed) | **Optional** | **No** | Simulating multi-subnet routers (`LAN A` on `VMnet2`, `LAN B` on `VMnet3`). |

---

## 3. Essential VMware Configuration Checklist for Lab VMs
1. **Guest OS Profile:** Select **Linux → Ubuntu 64-bit** when creating the VM so VMware enables paravirtualized `vmxnet3` networking and `pvscsi` storage drivers.
2. **Avoid Wi-Fi Bridging Pitfalls:** When using **Bridged** mode on a laptop, open **Edit → Virtual Network Editor** (or VM **Network Adapter → Configure Adapters**) and bind `VMnet0` explicitly to the wired Ethernet NIC rather than "Automatic" if the laptop switches between Wi-Fi and Ethernet.
3. **Disable Conflicting Host Services:** Ensure no external DHCP server on `Host-Only` / `Custom` segments conflicts with static IP exercises (`192.168.10.0/24` or `192.168.20.0/24`).
4. **Install `open-vm-tools`:** Inside Ubuntu Server, verify guest tools are active for clean shutdowns and accurate clock sync:
   ```bash
   sudo apt-get install -y open-vm-tools
   systemctl status open-vm-tools
   ```

---

## 4. Snapshot Best Practices (Fast Lab Recovery)
* **Take Snapshots Powered Off (or Quiesced):** Powered-off snapshots are smaller, faster to restore, and guarantee clean filesystem state.
* **Standard Naming Convention:**
  1. `01-OS-INSTALLED`: Fresh Ubuntu Server install with OpenSSH enabled.
  2. `02-BASELINE-WORKSHOP-READY`: All workshop packages (`apache2`, `ufw`, `curl`) and baseline firewall rules configured.
* **Classroom Reset Rule:** Never overwrite `02-BASELINE-WORKSHOP-READY` during a troubleshooting drill—always revert to it once grading is complete.
