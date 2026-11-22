# Linux Server Administration Command Reference
**Workshop 4: Linux Server Administration | Alijó IT Workshops**

---

## 1. System Information & Resource Monitoring

| Command | Purpose |
| :--- | :--- |
| `hostnamectl` | Display system hostname, OS version, and kernel architecture |
| `uptime` | Show system uptime, active user count, and 1/5/15-minute CPU load averages |
| `free -h` | Display total, used, and available RAM and swap in human-readable units |
| `df -h` | Check disk space usage across all mounted filesystems |
| `du -sh /var/log/*` | Summarize directory disk consumption inside `/var/log` |
| `lsblk` | List block storage devices, partitions, and mount points |
| `ps aux --sort=-%mem \| head -n 10` | List top 10 processes sorted by memory consumption |

---

## 2. Files, Text Search & Archives

| Command | Purpose |
| :--- | :--- |
| `ls -la /path` | List all files (including hidden dotfiles) with permissions, owner, and size |
| `grep -rn "Error" /var/log/` | Recursively search for matching text patterns across log files |
| `tail -n 30 -f /var/log/syslog` | Display the last 30 lines of a log and stream new entries live |
| `less /etc/ssh/sshd_config` | Safely page through configuration files without modifying them |
| `tar -czvf backup.tar.gz /etc/apache2` | Create a compressed `.tar.gz` archive of a configuration directory |

---

## 3. Users, Groups & POSIX Permissions

| Command | Purpose |
| :--- | :--- |
| `id username` | Display UID, primary GID, and all supplementary groups for a user |
| `sudo useradd -m -s /bin/bash alice` | Create a new user with a home directory and Bash login shell |
| `sudo passwd alice` | Set or update a user's password |
| `sudo groupadd webadmins` | Create a new security group |
| `sudo usermod -aG webadmins alice` | Append a user to a supplementary group (`-aG` prevents removing existing groups) |
| `sudo chown -R alice:webadmins /srv/app` | Recursively set user and group ownership on a directory |
| `sudo chmod 750 /srv/app` | Set `rwxr-x---` permissions (owner full, group read/traverse, others none) |
| `sudo chmod 640 /srv/app/config.env` | Set `rw-r-----` permissions on sensitive configuration files |

---

## 4. `systemd` Service Management & Journal Logs

| Command | Purpose |
| :--- | :--- |
| `systemctl status apache2` | Check service state, PID, memory usage, and recent log lines |
| `sudo systemctl start\|stop\|restart apache2` | Start, stop, or restart a service immediately |
| `sudo systemctl reload apache2` | Reload configuration files without dropping active connections |
| `sudo systemctl enable --now apache2` | Enable service at boot and start it immediately |
| `journalctl -u apache2 -n 50 --no-pager` | View the last 50 log entries for a specific unit |
| `journalctl -p err -b` | Show all error-level and higher messages since the current boot |

---

## 5. Networking & Host Firewall (`ufw`)

| Command | Purpose |
| :--- | :--- |
| `ip -br -4 addr` | Compact overview of network interfaces and IPv4 addresses |
| `ip route` | View kernel routing table and default gateway |
| `ss -tulpn` | List all listening TCP/UDP sockets with owning process names and PIDs |
| `curl -I http://localhost` | Send an HTTP `HEAD` request to inspect response status headers |
| `sudo ufw status numbered` | View active firewall rules with rule index numbers |
| `sudo ufw allow 80/tcp` | Permit inbound TCP traffic on port 80 |
| `sudo ufw delete <rule_number>` | Delete a specific firewall rule by its numbered index |
