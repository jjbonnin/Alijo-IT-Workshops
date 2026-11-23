# Physical Lab Server & Service Setup Guide (Instructor Reference)
**Workshop 3: Build and Configure a Network | Alijó IT Workshops**

---

## 1. Purpose
This guide documents how to prepare an Ubuntu Linux host to act as the local lab server (`192.168.10.10` or `192.168.20.10`) providing **HTTP**, **local DNS (`dnsmasq`)**, and optional **DHCP** services during the physical network lab phase.

---

## 2. Static IPv4 Configuration on Ubuntu Server Host
Identify the physical NIC name (`ip -br link`, e.g., `enp3s0` or `ens33`) and assign the static address:

```bash
# Replace <IFACE> with the actual interface name
sudo ip addr flush dev <IFACE>
sudo ip addr add 192.168.10.10/24 dev <IFACE>
sudo ip link set <IFACE> up
sudo ip route add default via 192.168.10.1
```

Verify configuration:
```bash
ip -br -4 addr
ip route
```

---

## 3. Local HTTP Intranet Service Setup
Create a lightweight web page and run Python's built-in HTTP server on port `8080` (no root privilege required):

```bash
mkdir -p ~/alijo-intranet
cat << 'EOF' > ~/alijo-intranet/index.html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Alijo Small Business Intranet</title></head>
<body>
  <h1>Alijo Small Business Intranet — Physical Lab Server</h1>
  <p>Status: Online (192.168.10.10:8080)</p>
</body>
</html>
EOF

nohup python3 -m http.server 8080 --directory ~/alijo-intranet > /tmp/alijo-http.log 2>&1 &
```

Verify locally:
```bash
curl -I http://127.0.0.1:8080
```

---

## 4. Optional Local DNS Service Setup (`dnsmasq`)
If your physical bench uses a dedicated local DNS server rather than `/etc/hosts`, configure `dnsmasq` to resolve `intranet.alijo.local`:

```bash
sudo apt-get update && sudo apt-get install -y dnsmasq

# Configure custom local domain resolution
sudo tee /etc/dnsmasq.d/alijo-lab.conf > /dev/null << 'EOF'
no-resolv
server=1.1.1.1
address=/intranet.alijo.local/192.168.10.10
listen-address=127.0.0.1,192.168.10.10
bind-interfaces
EOF

sudo systemctl restart dnsmasq
```

Verify local DNS resolution:
```bash
dig @192.168.10.10 intranet.alijo.local +short
# Expected output: 192.168.10.10
```

---

## 5. Firewall (`ufw`) Baseline Rules
Ensure `ufw` remains enabled while permitting local subnet access to HTTP (`8080/tcp`) and DNS (`53/udp`, `53/tcp`):

```bash
sudo ufw --force enable
sudo ufw allow from 192.168.10.0/24 to any port 8080 proto tcp
sudo ufw allow from 192.168.10.0/24 to any port 53
sudo ufw status numbered
```

---

## 6. Post-Workshop Teardown & Cleanup
Run these commands on the server host after the session to restore clean classroom defaults:

```bash
pkill -f "http.server 8080" || true
rm -rf ~/alijo-intranet /tmp/alijo-http.log
sudo rm -f /etc/dnsmasq.d/alijo-lab.conf
sudo systemctl stop dnsmasq 2>/dev/null || true
sudo ufw --force reset
sudo nmcli networking off && sudo nmcli networking on
```
