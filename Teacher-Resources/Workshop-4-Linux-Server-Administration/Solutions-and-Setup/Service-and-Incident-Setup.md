# Service Baseline & Incident (`INC-401`) Fault-Injection Setup
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Pre-Challenge Service Baseline Setup
Ensure `/srv/alijo-portal`, `/var/www/html/status.html`, and `Scripts/server_report.sh` exist in a healthy state before injecting faults:

```bash
sudo groupadd -f webadmins
sudo mkdir -p /srv/alijo-portal
echo "DB_PASS=AlijoSecret2026!" | sudo tee /srv/alijo-portal/.env >/dev/null
sudo chown root:webadmins /srv/alijo-portal /srv/alijo-portal/.env
sudo chmod 750 /srv/alijo-portal
sudo chmod 640 /srv/alijo-portal/.env

echo "<h1>Alijo Status: Operational</h1>" | sudo tee /var/www/html/status.html >/dev/null
sudo chown root:www-data /var/www/html/status.html
sudo chmod 644 /var/www/html/status.html
```

---

## 2. Fault-Injection Script (`INC-401` Outage Simulation)
Execute as `sudo` during the break prior to the Final Management Challenge:

```bash
#!/usr/bin/env bash
set -e

# Fault 1: Stop Apache2 web daemon
sudo systemctl stop apache2

# Fault 2: Lock /var/www/html/status.html (causes HTTP 403 once Apache starts)
sudo chown root:root /var/www/html/status.html
sudo chmod 600 /var/www/html/status.html

# Fault 3: Drift /srv/alijo-portal/.env to world-writable 666
sudo chown root:root /srv/alijo-portal/.env
sudo chmod 666 /srv/alijo-portal/.env

# Fault 4: Misconfigure UFW (allow Telnet 23/tcp, deny HTTP 80/tcp)
sudo ufw --force reset >/dev/null
sudo ufw default deny incoming >/dev/null
sudo ufw default allow outgoing >/dev/null
sudo ufw allow 22/tcp >/dev/null
sudo ufw allow 23/tcp >/dev/null
sudo ufw deny 80/tcp >/dev/null
sudo ufw --force enable >/dev/null

# Fault 5: Strip execute permission from server_report.sh
SCRIPT_PATH="./Workshop-4-Linux-Server-Administration/Scripts/server_report.sh"
[ -f "$SCRIPT_PATH" ] && chmod 644 "$SCRIPT_PATH"

echo "[+] INC-401 5-fault outage injected."
```
