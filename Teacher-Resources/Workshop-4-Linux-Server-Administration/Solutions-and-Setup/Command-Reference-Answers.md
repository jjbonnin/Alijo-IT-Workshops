# Command Reference & Worksheet Model Answers
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Baseline & Inspection Commands (`Server-Baseline-Record.md`)

| Metric | Reference Command | Expected Verification |
| :--- | :--- | :--- |
| **Hostname & OS** | `hostnamectl` | `Ubuntu 22.04` / `24.04 LTS` |
| **IPv4 Address** | `ip -br -4 addr` | Primary NIC `UP` with `/24` IPv4 |
| **Default Gateway** | `ip route show default` | `default via <GATEWAY_IP> dev <IFACE>` |
| **CPU & RAM** | `lscpu \| grep "Model name"` & `free -h` | `2` vCPUs, `2.0Gi` RAM |
| **Disk Usage** | `df -h /` | Root partition `< 50%` used |
| **Listening Ports** | `sudo ss -tulpn` | `sshd` (`:22`), `apache2` (`:80`) |

---

## 2. Users, Groups & Permissions Commands (`Users-Groups-and-Permissions-Record.md`)

```bash
# Group & user provisioning (preserving existing supplementary groups with -aG)
sudo groupadd -f webadmins
sudo groupadd -f auditors
sudo useradd -m -s /bin/bash dev_ana
sudo useradd -m -s /bin/bash audit_rui
sudo usermod -aG webadmins dev_ana
sudo usermod -aG auditors audit_rui

# Least-privilege directory and file hardening
sudo mkdir -p /srv/alijo-portal
sudo chown -R root:webadmins /srv/alijo-portal
sudo chmod 750 /srv/alijo-portal
sudo chmod 644 /srv/alijo-portal/index.html
sudo chmod 640 /srv/alijo-portal/.env
```

---

## 3. `systemd`, `ufw` & `cron` Commands (`Service-Management-Record.md` & `Bash-Script-Record.md`)

```bash
# Validate Apache config before graceful reload
sudo apache2ctl configtest
sudo systemctl reload apache2

# Hardened UFW baseline
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw --force enable

# Cron schedule (07:30 daily)
# 30 7 * * * /home/sysadmin/Alijo-IT-Workshops/Workshop-4-Linux-Server-Administration/Scripts/server_report.sh >> /var/log/server_health.log 2>&1
```
