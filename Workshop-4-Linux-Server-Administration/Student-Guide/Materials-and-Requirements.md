# Materials and Environment Requirements
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Required Lab Environment
To complete all modules and troubleshooting challenges in Workshop 4, verify that you have access to:
1. **Target Linux Server:**
   * **Ubuntu Server 22.04 LTS or 24.04 LTS** running inside a virtual machine (VMware Workstation/Fusion, VirtualBox, or Proxmox) or on a dedicated physical lab workstation.
   * **Minimum Resources:** 2 vCPUs, 2 GB RAM, 20 GB disk space, and active network connectivity (`NAT` or `Bridged`).
2. **Administrative Access:**
   * A non-root administrative user account (`sysadmin` or `ubtadmin`) with `sudo` privileges.
   * SSH access from your host terminal (`ssh sysadmin@<SERVER_IP>`) or direct console access.
3. **Clean Recovery Snapshot:**
   * Confirm that a clean baseline VM snapshot (`BASELINE - CLEAN UBUNTU SERVER`) exists before modifying firewall rules, user permissions, or service configuration files.

---

## 2. Required Software Packages
Run the following verification command on your Ubuntu Server to ensure all required CLI utilities and server daemons are installed:

```bash
sudo apt-get update && sudo apt-get install -y \
  openssh-server \
  apache2 \
  ufw \
  curl \
  tree \
  net-tools \
  iproute2 \
  dnsutils \
  acl
```

---

## 3. Baseline Verification Checklist
Before proceeding to `Linux-Command-Reference.md`, run these commands and record your initial system values in `Worksheets/Server-Baseline-Record.md`:

```bash
hostnamectl
lsb_release -a
ip -br -4 addr
ip route
df -h /
free -h
systemctl is-active ssh apache2
sudo ufw status
```

---

## 4. Safety & Operational Ground Rules
* **Do not work directly as `root`:** Always log in as your standard administrative account and prefix privileged actions with `sudo`.
* **Never disable `ufw` to bypass connectivity issues:** Keep the firewall active and add explicit port rules (`sudo ufw allow 80/tcp`).
* **Back up configuration files before editing:** Always create a `.bak` copy (`sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf.bak`) before making edits.
