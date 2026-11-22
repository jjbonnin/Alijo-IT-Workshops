# Ubuntu Server LTS Installation & Baseline Setup Guide
**04 — System Administration | Alijó IT Workshops**

---

## 1. Purpose
This reference guide walks through installing **Ubuntu Server 22.04 / 24.04 LTS** inside a virtual machine (or dedicated lab host) and configuring a clean, reproducible baseline for **Workshop 4: Linux Server Administration**.

---

## 2. Recommended Virtual Hardware Specifications
* **Operating System:** Ubuntu Server 22.04 LTS or 24.04 LTS (64-bit ISO)
* **vCPU:** 2 cores
* **RAM:** 2 GB (2048 MB) minimum; 4 GB recommended
* **Storage:** 25 GB virtual disk (Thin Provisioned / Dynamically Allocated)
* **Network Adapter:** NAT or Bridged (depending on classroom topology; see `VMware-Guide.md`)

---

## 3. Step-by-Step Installation Walkthrough

1. **Boot & Locale Selection:**
   * Boot from the Ubuntu Server ISO, select **English**, and choose your keyboard layout.
2. **Installation Type:**
   * Select **Ubuntu Server** (standard installation, not minimized) so essential administrative utilities (`man`, `curl`, `iproute2`, `ufw`) are included.
3. **Network Configuration:**
   * Leave DHCP enabled during initial installation to fetch updates, or assign a static IPv4 address (e.g., `192.168.50.10/24`, Gateway `192.168.50.1`, DNS `1.1.1.1`).
4. **Storage Configuration:**
   * Select **Use an entire disk** with default LVM layout and confirm disk formatting.
5. **Profile & Credentials Setup:**
   * **Your name:** `Alijo Admin`
   * **Server's name:** `alijo-srv01`
   * **Username:** `sysadmin` *(or classroom standard `ubtadmin`)*
   * **Password:** Strong lab password documented in instructor sheet
6. **SSH Setup (Critical):**
   * Check **`[X] Install OpenSSH server`** so you can administer the server remotely via SSH from your workstation terminal.
7. **Featured Server Snaps:**
   * Leave unselected during initial OS install; required packages (`apache2`, `ufw`, `tree`, `net-tools`) will be installed via `apt`.

---

## 4. Post-Installation Baseline Configuration

Log in via console or SSH (`ssh sysadmin@<SERVER_IP>`) and run the following baseline commands:

```bash
# 1. Update package index and apply security updates
sudo apt-get update && sudo apt-get upgrade -y

# 2. Install core diagnostic and web server packages for Workshop 4
sudo apt-get install -y apache2 ufw curl tree net-tools dnsutils

# 3. Enable host firewall while permitting SSH and HTTP
sudo ufw allow OpenSSH
sudo ufw allow 'Apache'
sudo ufw --force enable

# 4. Verify baseline status
hostnamectl
ip -br -4 addr
sudo ufw status verbose
systemctl is-active ssh apache2
```

---

## 5. Take the Baseline Snapshot
Before starting any lab exercises or fault injections:
1. Shut down cleanly (`sudo shutdown -h now`) or pause the VM.
2. Create a snapshot named **`BASELINE - CLEAN UBUNTU SERVER`**.
3. If an exercise breaks networking or services beyond recovery, revert to this snapshot in seconds.
