# Worksheet 3: Service Management & Firewall Record
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## Student Details
* **Student Name(s):** 
* **Date:** 

---

## 1. Core `systemd` Service States (`systemctl`)
Record the runtime (`is-active`), boot (`is-enabled`), and Main PID values for `ssh` and `apache2`:

| Service Unit | `systemctl is-active` | `systemctl is-enabled` | Main PID (`systemctl status`) |
| :--- | :--- | :--- | :--- |
| **`ssh.service`** | | | |
| **`apache2.service`** | | | |

---

## 2. Active Listening Sockets (`sudo ss -tulpn`)
Record the local address, port, and process name bound to TCP ports `22` and `80`:

| Protocol | Local Address : Port | Process Name & PID |
| :--- | :--- | :--- |
| TCP | `*:22` or `0.0.0.0:22` | |
| TCP | `*:80` or `:::80` | |

---

## 3. Apache2 Configuration Syntax & HTTP Validation
* **Output of `sudo apache2ctl configtest`:** 
* **HTTP Status Line from `curl -i http://127.0.0.1`:** 

**Question:** What is the operational difference between running `sudo systemctl reload apache2` versus `sudo systemctl restart apache2` on a live web server?
* **Answer:** 

---

## 4. Host Firewall Configuration (`sudo ufw status numbered`)
Record your active `ufw` default policies and numbered rules:

* **Default Incoming Policy:** 
* **Default Outgoing Policy:** 

| Rule # | To (Port / Protocol) | Action | From |
| :--- | :--- | :--- | :--- |
| `[ 1]` | | | |
| `[ 2]` | | | |
| `[ 3]` | | | |
| `[ 4]` | | | |
