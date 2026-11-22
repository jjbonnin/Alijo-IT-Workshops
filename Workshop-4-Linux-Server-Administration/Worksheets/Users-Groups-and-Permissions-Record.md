# Worksheet 2: Users, Groups, and Permissions Record
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## Student Details
* **Student Name(s):** 
* **Date:** 

---

## 1. User & Group Identity Verification (`id`)
Paste or transcribe the output of `id dev_ana` and `id audit_rui` after assigning supplementary groups:

| User Account | UID | Primary Group | Supplementary Group(s) |
| :--- | :--- | :--- | :--- |
| **`dev_ana`** | | | |
| **`audit_rui`** | | | |

**Question:** Why is it important to run `sudo usermod -aG webadmins dev_ana` with the `-a` (append) flag instead of `-G` alone?
* **Answer:** 

---

## 2. Directory & File Ownership Audit (`ls -la /srv/alijo-portal`)
Record the exact permission strings, owner, and group for `/srv/alijo-portal` and its files:

| Path | Symbolic Permissions (e.g., `drwxr-x---`) | Octal Mode | Owner | Group |
| :--- | :--- | :--- | :--- | :--- |
| `/srv/alijo-portal` | | | | |
| `/srv/alijo-portal/index.html` | | | | |
| `/srv/alijo-portal/.env` | | | | |

---

## 3. Access Control Boundary Test Results
Record the observed result (`Succeeded` + output or `Permission denied`) for each test command:

| Test Command | Expected Outcome | Observed Result |
| :--- | :--- | :--- |
| `sudo -u dev_ana cat /srv/alijo-portal/index.html` | Succeeds (reads HTML) | |
| `sudo -u dev_ana cat /srv/alijo-portal/.env` | Succeeds (reads `.env`) | |
| `sudo -u audit_rui ls -la /srv/alijo-portal` | Blocked (`Permission denied`) | |
| `sudo -u audit_rui cat /srv/alijo-portal/.env` | Blocked (`Permission denied`) | |

---

## 4. Reflection Question
If `/srv/alijo-portal` were changed from `750` (`rwxr-x---`) to `755` (`rwxr-xr-x`), while `.env` remained `640` (`rw-r-----`), could `audit_rui` list the filenames inside `/srv/alijo-portal`? Could `audit_rui` read the contents of `.env`? Explain briefly.
* **Answer:**
