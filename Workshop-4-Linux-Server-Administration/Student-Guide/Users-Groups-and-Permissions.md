# Managing Users, Groups, and POSIX Permissions
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. Objective
In this module, you will implement role-based access control on your Ubuntu Server using local users, security groups, and least-privilege POSIX permissions. You will create two departmental accounts, configure a shared web deployment directory for `webadmins`, and verify that unauthorized users are blocked from reading sensitive configuration secrets.

---

## 2. Understanding Linux POSIX Permissions
Every file and directory in Linux stores three permission sets—**Owner (`u`)**, **Group (`g`)**, and **Others (`o`)**—using three permission bits:

| Symbol | Octal Value | Meaning on a Regular File | Meaning on a Directory |
| :--- | :--- | :--- | :--- |
| **`r`** (Read) | `4` | View file contents (`cat`, `less`) | List filenames inside directory (`ls`) |
| **`w`** (Write) | `2` | Modify or truncate file contents | Create, rename, or delete files inside directory |
| **`x`** (Execute) | `1` | Run file as a program or shell script | Enter/traverse directory (`cd`) and access metadata |

### Standard Server Permission Profiles
* **`755` (`rwxr-xr-x`):** Public web directories (`/var/www/html`) and executable scripts.
* **`750` (`rwxr-x---`):** Restricted team project directories (owner full control, group read/enter, others denied).
* **`644` (`rw-r--r--`):** Standard non-sensitive configuration files and static HTML pages.
* **`640` (`rw-r-----`):** Sensitive application config files containing database passwords or API keys.
* **`600` (`rw-------`):** Private SSH keys (`~/.ssh/id_ed25519`) and root-only credential files.

---

## 3. Step-by-Step Lab Tasks

### Task 1: Create Departmental Users and Security Groups
1. Create two new groups (`webadmins` and `auditors`):
   ```bash
   sudo groupadd webadmins
   sudo groupadd auditors
   ```
2. Create two user accounts (`dev_ana` and `audit_rui`) with home directories and Bash login shells:
   ```bash
   sudo useradd -m -s /bin/bash dev_ana
   sudo useradd -m -s /bin/bash audit_rui
   ```
3. Set temporary lab passwords for both accounts:
   ```bash
   sudo passwd dev_ana
   sudo passwd audit_rui
   ```
4. Assign `dev_ana` to `webadmins` and `audit_rui` to `auditors` (always use `-aG` so existing group memberships are preserved):
   ```bash
   sudo usermod -aG webadmins dev_ana
   sudo usermod -aG auditors audit_rui
   ```
5. Verify group memberships:
   ```bash
   id dev_ana
   id audit_rui
   ```

---

### Task 2: Provision a Restricted Web Deployment Directory
1. Create `/srv/alijo-portal` and an internal secrets file:
   ```bash
   sudo mkdir -p /srv/alijo-portal
   echo "<h1>Alijo Internal Portal v1.0</h1>" | sudo tee /srv/alijo-portal/index.html
   echo "DB_PASS=AlijoSecret2026!" | sudo tee /srv/alijo-portal/.env
   ```
2. Set ownership to `root:webadmins` and apply least-privilege permissions (`750` on the directory, `644` on `index.html`, and `640` on `.env`):
   ```bash
   sudo chown -R root:webadmins /srv/alijo-portal
   sudo chmod 750 /srv/alijo-portal
   sudo chmod 644 /srv/alijo-portal/index.html
   sudo chmod 640 /srv/alijo-portal/.env
   ls -la /srv/alijo-portal
   ```

---

### Task 3: Test Access Boundaries (`dev_ana` vs. `audit_rui`)
1. Test reading both files as **`dev_ana`** (member of `webadmins` — should **succeed**):
   ```bash
   sudo -u dev_ana cat /srv/alijo-portal/index.html
   sudo -u dev_ana cat /srv/alijo-portal/.env
   ```
2. Test accessing `/srv/alijo-portal` as **`audit_rui`** (not in `webadmins` — should return **`Permission denied`**):
   ```bash
   sudo -u audit_rui ls -la /srv/alijo-portal
   sudo -u audit_rui cat /srv/alijo-portal/.env
   ```

---

## 4. Deliverable
Document all `id` outputs, `ls -la /srv/alijo-portal` permissions, and access verification test results in **`Worksheets/Users-Groups-and-Permissions-Record.md`**.
