# Bare-Metal Physical Linux Server Setup & Operations Guide
**04 — System Administration | Alijó IT Workshops**

---

## 1. Purpose
This reference guide covers deploying, verifying, and maintaining Ubuntu Linux directly on physical hardware (desktop workstations, mini-PCs, or rack servers) when running bare-metal labs for **Workshop 3** and **Workshop 4**.

---

## 2. Physical Hardware & BIOS/UEFI Preparation
1. **Boot Media:** Flash the official Ubuntu Server or Ubuntu Desktop LTS ISO onto a USB drive using `dd`, Ventoy, BalenaEtcher, or Rufus (GPT partition scheme for UEFI systems).
2. **Firmware Settings:**
   * Enable **UEFI Boot** (disable Legacy/CSM unless required by older lab hardware).
   * Enable **Intel VT-x / AMD-V** virtualization extensions in BIOS/UEFI in case nested VMs or containers are used later.
   * Enable **Wake-on-LAN (WoL)** and **AC Power Recovery → Power On** if administering lab hosts remotely.

---

## 3. Identifying Physical Hardware Interfaces on Linux
Unlike virtual machines with predictable `ens33` or `eth0` names, physical Linux machines use **Predictable Network Interface Names** tied to PCI bus or motherboard slot locations (e.g., `enp3s0`, `eno1`, `wlp2s0`).

```bash
# List physical network interfaces and link states (UP vs DOWN)
ip -br link

# Inspect PCI Ethernet and Wi-Fi hardware controllers
lspci | grep -iE "ethernet|network"

# Check physical link speed, duplex, and cable detection on an interface
sudo ethtool enp3s0 | grep -E "Speed|Duplex|Link detected"

# List physical disks and partitions (NVMe vs SATA)
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT
```

---

## 4. Persistent Static IP Configuration with Netplan
On Ubuntu Server physical hosts, configure persistent static IPv4 settings via `/etc/netplan/01-netcfg.yaml` so settings survive reboots:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
      dhcp4: no
      addresses:
        - 192.168.10.10/24
      routes:
        - to: default
          via: 192.168.10.1
      nameservers:
        addresses:
          - 192.168.10.10
          - 1.1.1.1
```

Apply and test safely (automatically reverts after 120 seconds if disconnected):
```bash
sudo chmod 600 /etc/netplan/01-netcfg.yaml
sudo netplan try
sudo netplan apply
```

---

## 5. Bare-Metal Lab Safety & Recovery Rules
* **No VM Snapshots on Bare Metal:** Because physical installations cannot roll back with a single click, always back up configuration files before editing (`sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak`).
* **Keep Local Console Access Ready:** Always retain a local keyboard/monitor (or IPMI/KVM) on physical lab servers in case a network or firewall misconfiguration drops SSH connectivity.
* **Post-Lab Teardown:** Remove temporary static IP files, stop lab daemons, and run `sudo ufw --force reset` before powering off physical bench machines.
