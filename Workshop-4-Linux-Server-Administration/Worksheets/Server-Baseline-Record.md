# Worksheet 1: Server Baseline Record
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## Student & Environment Details
* **Student Name(s):** 
* **Date:** 
* **Deployment Type:** `[ ] VMware VM`  `[ ] VirtualBox / Proxmox`  `[ ] Bare-Metal Physical Host`
* **VM Network Mode:** `[ ] NAT`  `[ ] Bridged`  `[ ] Host-Only / Custom`

---

## 1. Host Identity & Operating System (`hostnamectl` / `lsb_release -a`)
Fill in the baseline values recorded from your Ubuntu Server terminal:

| Parameter | Recorded Value | Command Used |
| :--- | :--- | :--- |
| **Static Hostname** | | `hostnamectl` |
| **Operating System & Version** | | `lsb_release -d` |
| **Linux Kernel Release** | | `uname -r` |
| **CPU Architecture** | | `uname -m` |
| **System Uptime** | | `uptime -p` |

---

## 2. Compute, Memory & Storage Baseline (`free -h` / `df -h` / `lsblk`)

| Metric | Recorded Value |
| :--- | :--- |
| **vCPU / Core Count (`nproc`)** | |
| **Total RAM (`free -h`)** | |
| **Available RAM (`free -h`)** | |
| **Root Filesystem (`/`) Total Size (`df -h /`)** | |
| **Root Filesystem (`/`) Used % (`df -h /`)** | |

---

## 3. Network Interface & Routing Baseline (`ip -br -4 addr` / `ip route`)

| Parameter | Recorded Value |
| :--- | :--- |
| **Primary Interface Name (e.g., `ens33`, `enp0s3`)** | |
| **IPv4 Address & CIDR Prefix** | |
| **Default Gateway IP** | |
| **Configured DNS Server (`resolvectl status`)** | |

---

## 4. Baseline Services, Firewall & Snapshot Verification
* **OpenSSH Daemon (`systemctl is-active ssh`):** 
* **Apache2 Web Server (`systemctl is-active apache2`):** 
* **UFW Firewall Initial Status (`sudo ufw status`):** 
* **Clean Baseline Snapshot Created?** `[ ] Yes — Snapshot Name: _______________________`
