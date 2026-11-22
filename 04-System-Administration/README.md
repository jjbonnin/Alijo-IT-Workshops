# 04 — Linux System Administration & Server Operations
**Alijó IT Workshops | Reference Module**

---

## 1. Module Overview
This module provides deployment and operations documentation for administering Ubuntu Linux servers in both **virtualized (VMware)** and **bare-metal physical** environments. It serves as the foundational reference for **Workshop 4: Linux Server Administration**.

---

## 2. Reference Guides in This Directory
* **`Reference-Guides/Ubuntu-Server-VM-Setup.md`:** Step-by-step installation, static networking, OpenSSH hardening, and baseline package configuration for Ubuntu Server LTS.
* **`Reference-Guides/VMware-Guide.md`:** Virtual network adapter modes (`NAT`, `Bridged`, `Host-Only`), snapshot management, and resource allocation best practices for lab VMs.
* **`Reference-Guides/Physical-Linux-Guide.md`:** Bare-metal installation considerations, hardware/NIC identification, storage partitioning, and physical console recovery.

---

## 3. Core Linux Server Administration Domains

| Domain | Key Concepts | Essential Commands |
| :--- | :--- | :--- |
| **System Health & Resources** | CPU load, RAM/swap usage, disk capacity, uptime | `uptime`, `free -h`, `df -h`, `lsblk`, `top` / `htop` |
| **Users, Groups & Permissions** | Least privilege, `sudo` delegation, POSIX file modes (`rwx`) | `useradd`, `usermod -aG`, `passwd`, `chmod`, `chown`, `id` |
| **Service Management (`systemd`)** | Starting, stopping, enabling at boot, inspecting unit status | `systemctl status`, `systemctl enable --now`, `systemctl restart` |
| **Logs & Diagnostics** | Kernel messages, service journals, authentication logs | `journalctl -u <service> -xe`, `tail -f /var/log/syslog`, `dmesg` |
| **Network & Firewall (`ufw`)** | Interface status, listening sockets, host-based packet filtering | `ip -br -4 addr`, `ss -tulpn`, `ufw status numbered`, `ufw allow` |

---

## 4. Operational Best Practices for Lab & Production Servers
1. **Snapshot Before Major Changes:** Always capture a clean baseline snapshot (`BASELINE - CLEAN`) before modifying firewall rules, service configs, or user permissions.
2. **Validate Configuration Syntax Before Restarting Services:** Use built-in validators (`sshd -t`, `apache2ctl configtest`, `nginx -t`) prior to running `systemctl restart` so a typo does not lock you out or break a live service.
3. **Never Disable Host Firewalls to Troubleshoot:** Keep `ufw` active and open only the required port/protocol (`sudo ufw allow 22/tcp`, `sudo ufw allow 80/tcp`).

---

## 5. Related Workshop Materials
* **Hands-On Workshop:** `../Workshop-4-Linux-Server-Administration/`
* **Instructor Guide & Solutions:** `../Teacher-Resources/Workshop-4-Linux-Server-Administration/`
