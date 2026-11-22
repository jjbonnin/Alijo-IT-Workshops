# Managing `systemd` Services and the `ufw` Host Firewall
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Objective
In this module, you will manage background services on Ubuntu Server using `systemd` (`systemctl`), deploy a custom Apache2 virtual host / landing page, validate service configuration syntax before restarting daemons, and enforce host-level network filtering with **Uncomplicated Firewall (`ufw`)**.

---

## 2. Understanding `systemd` Service States
* **`active (running)` vs. `inactive (dead)`:** Indicates whether the daemon is currently running in memory right now.
* **`enabled` vs. `disabled`:** Indicates whether the service will start automatically when the server reboots.
* **`reload` vs. `restart`:**
  * `systemctl reload apache2` tells Apache to re-read its configuration files gracefully without dropping active user sessions.
  * `systemctl restart apache2` terminates the daemon completely and launches a new process.

---

## 3. Step-by-Step Lab Tasks

### Task 1: Inspect and Enable Core Services (`ssh` and `apache2`)
1. Check the runtime and boot status of `ssh` and `apache2`:
   ```bash
   systemctl status ssh --no-pager
   systemctl status apache2 --no-pager
   ```
2. Ensure both services are started and enabled across reboots:
   ```bash
   sudo systemctl enable --now ssh
   sudo systemctl enable --now apache2
   ```
3. Verify that both daemons are bound and listening on TCP ports `22` and `80`:
   ```bash
   sudo ss -tulpn | grep -E ':22|:80'
   ```

---

### Task 2: Configure & Validate a Custom Web Page on Apache2
1. Back up the default Apache site configuration and landing page:
   ```bash
   sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf.bak
   sudo cp /var/www/html/index.html /var/www/html/index.html.bak
   ```
2. Deploy a custom status page for the Alijó Operations Server:
   ```bash
   cat << 'EOF' | sudo tee /var/www/html/index.html
   <!DOCTYPE html>
   <html lang="en">
   <head><meta charset="UTF-8"><title>Alijo Operations Server</title></head>
   <body>
     <h1>Alijo Operations Server — Online</h1>
     <p>Managed via systemd & protected by UFW.</p>
   </body>
   </html>
   EOF
   ```
3. Validate Apache configuration syntax **before** reloading:
   ```bash
   sudo apache2ctl configtest
   ```
   *(Expected output: `Syntax OK`)*
4. Reload Apache2 and verify HTTP delivery locally:
   ```bash
   sudo systemctl reload apache2
   curl -i [http://127.0.0.1](http://127.0.0.1)
   ```

---

### Task 3: Configure Least-Privilege Host Firewall Rules (`ufw`)
1. Inspect the current firewall status:
   ```bash
   sudo ufw status verbose
   ```
2. Set secure default policies (deny all unsolicited inbound traffic, allow outbound traffic):
   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   ```
3. Explicitly permit SSH (`22/tcp`) **before** enabling `ufw` so you do not lock yourself out, then allow HTTP (`80/tcp`):
   ```bash
   sudo ufw allow 22/tcp comment 'Allow SSH administration'
   sudo ufw allow 80/tcp comment 'Allow Apache HTTP'
   sudo ufw --force enable
   ```
4. Verify active rules and test external HTTP access from your host machine:
   ```bash
   sudo ufw status numbered
   ```

---

## 4. Deliverable
Record your service statuses, `ss -tulpn` listening port output, `apache2ctl configtest` result, and `ufw status numbered` table in **`Worksheets/Service-Management-Record.md`**.
