# Ubuntu Server VM Baseline Setup Guide (SSH, Netplan & Webmin)
**Alijó IT Workshops | Shared Virtualization Reference**

---

## 1. Purpose & Hybrid Network Architecture
This guide documents the complete setup procedure to prepare a clean **Ubuntu Server** virtual machine in **Oracle VM VirtualBox** with remote CLI access (**SSH**), web-based system management (**Webmin**), and persistent dual-NIC networking (**Netplan**).

| Adapter | Interface | VirtualBox Mode | IPv4 Address | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Adapter 1** | `enp0s3` | **NAT** | `10.0.2.15/24` (DHCP) | Outbound Internet access for `apt` updates and package installation. |
| **Adapter 2** | `enp0s8` | **Host-Only Adapter** | `192.168.56.102/24` (Static) | Direct host-to-VM management link (SSH & Webmin) without port forwarding. |

---

## 2. Step 1: VirtualBox Network Configuration
Before booting (or while configuring the VM in VirtualBox Manager):
1. Open **Settings → Network** for your Ubuntu Server VM.
2. **Adapter 1:** Enable Network Adapter → Attached to **NAT** (`enp0s3`).
3. **Adapter 2:** Enable Network Adapter → Attached to **Host-only Adapter** (`enp0s8`).
4. Boot the VM and log in via the local VirtualBox console.

---

## 3. Step 2: Configure Persistent Static IP with Netplan (`enp0s8`)
Configure Netplan so `enp0s8` always comes up at boot with the static IP `192.168.56.102/24`, without defining a second default gateway (keeping outbound Internet traffic routed through `enp0s3`):

```bash
# Bring up the secondary interface immediately
sudo ip link set enp0s8 up

# Create persistent Netplan configuration for enp0s8
sudo tee /etc/netplan/60-enp0s8.yaml > /dev/null << 'EOF'
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s8:
      dhcp4: no
      addresses:
        - 192.168.56.102/24
EOF

# Restrict file permissions and apply configuration
sudo chmod 600 /etc/netplan/60-enp0s8.yaml
sudo netplan apply
```

### Verification
Confirm both interfaces are `UP` and only one default route exists via `enp0s3`:
```bash
ip -br -4 addr
ip route
```
* Expected `enp0s3`: `UP 10.0.2.15/24`
* Expected `enp0s8`: `UP 192.168.56.102/24`
* Expected default route: `default via 10.0.2.2 dev enp0s3`

---

## 4. Step 3: Enable OpenSSH Server & Base CLI Utilities
Ensure `openssh-server` and the diagnostic/web utilities required for the workshops are installed and running:

```bash
sudo apt update && sudo apt install -y openssh-server curl python3 ufw net-tools lsof nginx
sudo systemctl enable --now ssh
```

### Verification
Confirm the SSH daemon is active and listening on TCP port `22`:
```bash
systemctl status ssh --no-pager
ss -tulpn | grep :22
```

Test direct SSH access from the **Windows Host** (`CMD` or `PowerShell`):
```cmd
ssh ubtadmin@192.168.56.102
```

---

## 5. Step 4: Install Webmin (Web-Based Administration)
Configure the official Webmin repository and install `webmin` on the Ubuntu Server VM:

```bash
curl -o webmin-setup-repo.sh [https://raw.githubusercontent.com/webmin/webmin/master/webmin-setup-repo.sh](https://raw.githubusercontent.com/webmin/webmin/master/webmin-setup-repo.sh)
sudo sh webmin-setup-repo.sh -f
sudo apt install -y webmin --install-recommends
rm -f webmin-setup-repo.sh
```

### Verification
Check that the Webmin service is running on TCP port `10000`:
```bash
sudo systemctl status webmin --no-pager
ss -tulpn | grep :10000
```

---

## 6. Step 5: Configure Firewall (`ufw`)
Allow **SSH (`22/tcp`)** and **Webmin (`10000/tcp`)** explicitly before enabling `ufw` so remote sessions are never dropped:

```bash
sudo ufw allow 22/tcp
sudo ufw allow 10000/tcp
sudo ufw --force enable
sudo ufw status verbose
```

### Verification
From the **Windows Host** browser, open:
* `https://192.168.56.102:10000`
* Accept the self-signed TLS certificate warning and log in with your Ubuntu system credentials (`ubtadmin`).

---

## 7. Step 6: Prepare Workshop 2 Lab Assets
Create the local practice directory and baseline files (`sample-service.log` and `diagnostic_script.py`) on the VM:

```bash
mkdir -p ~/w2-lab/Assets

cat << 'EOF' > ~/w2-lab/Assets/sample-service.log
Nov 22 09:14:02 ubuntu-lab systemd[1]: Starting A high performance web server and a reverse proxy server...
Nov 22 09:14:02 ubuntu-lab nginx[2411]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
Nov 22 09:14:02 ubuntu-lab nginx[2411]: nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
Nov 22 09:14:03 ubuntu-lab nginx[2411]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
Nov 22 09:14:03 ubuntu-lab nginx[2411]: nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
Nov 22 09:14:04 ubuntu-lab nginx[2411]: nginx: [emerg] still could not bind()
Nov 22 09:14:04 ubuntu-lab systemd[1]: nginx.service: Control process exited, code=exited, status=1/FAILURE
Nov 22 09:14:04 ubuntu-lab systemd[1]: nginx.service: Failed with result 'exit-code'.
Nov 22 09:14:04 ubuntu-lab systemd[1]: Failed to start A high performance web server and a reverse proxy server.
EOF

cat << 'EOF' > ~/w2-lab/Assets/diagnostic_script.py
#!/usr/bin/env python3
"""
System Diagnostic Script (Broken Version for Workshop 2 - Scenario 02)
Purpose: Check disk space, network connectivity, and critical service status on Ubuntu.
WARNING: This script contains intentional syntax, logic, and security bugs for debugging practice.
"""

import os
import shutil

def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    # BUG 1 (Logic): Divides free by total instead of used by total, inverting the percentage
    percent_used = (free / total) * 100
    print(f"[DISK] Disk usage on {path}: {percent_used:.1f}%")
    if percent_used > 85:
        print("[ALERT] Disk usage is critically high!")
    else:
        print("[OK] Disk space is within normal limits.")

# BUG 2 (Syntax): Missing colon at the end of function definition
def check_network(host="127.0.0.1")
    # BUG 3 (Unsafe/Fragile Shell Call): Uses os.system without validation and infinite ping on Linux (-c missing)
    response = os.system("ping " + host)
    if response == 0:
        print(f"[NET] Host {host} is reachable.")
    else:
        print(f"[NET] Host {host} is unreachable.")

def check_service(service_name="ssh"):
    # BUG 4 (Logic/Return Code): systemctl is-active returns 0 when active, non-zero when inactive
    status = os.system(f"systemctl is-active --quiet {service_name}")
    if status != 0:
        print(f"[SERVICE] {service_name} is RUNNING.")
    else:
        print(f"[SERVICE] {service_name} is STOPPED or FAILED.")

if __name__ == "__main__":
    print("=== Starting Ubuntu System Diagnostic ===")
    check_disk_usage("/")
    check_network("8.8.8.8")
    check_service("ssh")
    print("=== Diagnostic Complete ===")
EOF

ls -lh ~/w2-lab/Assets/
```

---

## 8. Step 7: Capture Clean Baseline Snapshot
Before introducing intentional faults for lab scenarios, take a clean snapshot from the **Windows Host** (`CMD`):

```cmd
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" snapshot "NOMBRE_DE_LA_VM" take "BASELINE – BEFORE WORKSHOP" --description "Ubuntu Server clean state: Netplan 192.168.56.102, SSH (22), Webmin (10000), UFW, and W2 Assets"
```

*(Refer to `Snapshots-and-Recovery.md` for full restore instructions between lab sessions.)*
