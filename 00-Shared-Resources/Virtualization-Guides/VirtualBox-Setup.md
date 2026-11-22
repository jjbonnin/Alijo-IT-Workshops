# VirtualBox Lab Setup Guide
**Alijó IT Workshops | Shared Virtualization Reference**

## 1. Purpose
This guide defines the standard configuration for running virtual machines (VMs) in Oracle VM VirtualBox across the Alijó IT Workshops. Following these settings ensures an isolated, safe, and reproducible lab environment.

## 2. Recommended VM Baseline Specifications
* **Hypervisor:** Oracle VM VirtualBox (latest stable release)
* **CPU:** 2 vCPUs
* **RAM:** 2048 MB – 4096 MB (2–4 GB depending on host capacity)
* **Storage:** 20 GB dynamically allocated virtual disk (`.vdi`)
* **Guest Additions:** Installed (enables clipboard sharing and display resizing)

## 3. Network Configuration Rules (Crucial for Safety)
> **⚠️ Safety Warning:** Never bridge an unconfigured experimental VM directly to the school production LAN unless explicitly instructed.

Choose the network mode specified by your workshop guide:
1. **NAT / NAT Network (Default for Workshop 1 & Workshop 2):**
   * Gives the VM outbound internet access (for DNS and `ping 1.1.1.1` tests) while isolating it behind the host's IP.
   * Ideal when teams work independently on a single VM.
2. **Internal Network / Host-Only Adapter (Used for multi-VM labs such as Workshop 3 & 4):**
   * Isolates traffic strictly between VMs on the same host PC without touching external networks.

## 4. Simulating a Cable Disconnect (Used in Troubleshooting Labs)
To simulate a physical network disconnection inside VirtualBox without shutting down the VM:
1. In the VM window menu, go to **Devices** → **Network**.
2. Uncheck **Connect Network Adapter** (or right-click the network icon in the bottom-right status bar of the VM window and click **Connect Network Adapter** to toggle it).
