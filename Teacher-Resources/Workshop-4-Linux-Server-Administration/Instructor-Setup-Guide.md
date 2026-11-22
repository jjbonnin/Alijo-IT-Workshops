# Instructor Lab Setup & Fault-Injection Guide
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Golden VM Image Preparation
Before the workshop begins, prepare a clean Ubuntu Server 22.04 LTS or 24.04 LTS template VM with the following baseline configuration:
* **Resources:** 2 vCPUs, 2 GB RAM, 20 GB virtual disk, Bridged or NAT networking.
* **Admin Account:** `sysadmin` (or `ubtadmin`) with passwordless or standard `sudo` privileges.
* **Installed Packages:**
  ```bash
  sudo apt-get update && sudo apt-get install -y \
    openssh-server apache2 ufw curl tree net-tools iproute2 dnsutils acl
  ```
* **Snapshot:** Power off or pause the clean VM and take a baseline snapshot named `BASELINE - CLEAN UBUNTU SERVER` so students can reset in under 30 seconds if needed.

---

## 2. Automated Fault-Injection Script (For Final Management Challenge)
Run the following script as `sudo` on student VMs right before **Block 5 (`Final-Management-Challenge.md`)** to inject all five realistic production faults cleanly:

```bash
#!/usr/bin/env bash
# Workshop 4 — Final Challenge Fault Injector (Instructor Use Only)
set -e

echo "[*] Preparing baseline portal artifacts if absent..."
sudo groupadd -f webadmins
sudo mkdir -p /srv/alijo-portal
echo "DB_PASS=AlijoSecret2026!" | sudo tee /srv/alijo-portal/.env >/dev/null
echo "<h1>Alijo Status: Operational</h1>" | sudo tee /var/www/html/status.html >/dev/null

echo "[*] Injecting Fault 1: Stopping Apache2 service..."
sudo systemctl stop apache2

echo "[*] Injecting Fault 2: Restricting /var/www/html/status.html to root:root 600..."
sudo chown root:root /var/www/html/status.html
sudo chmod 600 /var/www/html/status.html

echo "[*] Injecting Fault 3: Drifting /srv/alijo-portal/.env permissions to 666..."
sudo chown root:root /srv/alijo-portal/.env
sudo chmod 666 /srv/alijo-portal/.env

echo "[*] Injecting Fault 4: Blocking HTTP (80/tcp) and allowing Telnet (23/tcp) in UFW..."
sudo ufw --force reset >/dev/null
sudo ufw default deny incoming >/dev/null
sudo ufw default allow outgoing >/dev/null
sudo ufw allow 22/tcp >/dev/null
sudo ufw allow 23/tcp >/dev/null
sudo ufw deny 80/tcp >/dev/null
sudo ufw --force enable >/dev/null

echo "[*] Injecting Fault 5: Removing execute bit from server_report.sh..."
if [ -f ./Workshop-4-Linux-Server-Administration/Scripts/server_report.sh ]; then
    chmod 644 ./Workshop-4-Linux-Server-Administration/Scripts/server_report.sh
fi

echo "[+] All 5 faults injected successfully. Ready for student troubleshooting!"
```

---

## 3. Classroom Verification Tips
* Verify from the instructor laptop that `curl -I http://<STUDENT_VM_IP>/status.html` times out immediately after fault injection and returns `HTTP/1.1 200 OK` once the student completes remediation.
