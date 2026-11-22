#!/usr/bin/env python3
"""
Challenge 2 Reference Solution: Fixed System Diagnostic Script
Workshop 2: AI as an IT Technician Assistant
Location: Teacher-Resources/Workshop-2-AI-IT-Technician-Assistant/Solutions-and-Setup/Challenge-2-Script-Solution.py

Summary of Fixes Applied to Assets/diagnostic_script.py:
  1. Logic Fix (Disk Usage): Replaced (free / total) * 100 with (used / total) * 100.
  2. Syntax Fix (Function Header): Added missing colon ':' on def check_network(...).
  3. Safety & Reliability Fix (Ping): Replaced unbounded os.system("ping " + host)
     with subprocess.run(["ping", "-c", "1", "-W", "2", host], ...) to prevent
     infinite hanging on Linux and avoid shell injection.
  4. Logic Fix (Service Exit Code): Inverted check so returncode == 0 reports RUNNING
     (systemctl is-active --quiet returns 0 when active, non-zero otherwise).
"""

import shutil
import subprocess
import sys


def check_disk_usage(path: str = "/") -> bool:
    """Calculate actual disk usage percentage and report status."""
    total, used, _ = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    print(f"[DISK] Disk usage on {path}: {percent_used:.1f}%")
    if percent_used > 85.0:
        print("[ALERT] Disk usage is critically high!")
        return False
    print("[OK] Disk space is within normal limits.")
    return True


def check_network(host: str = "127.0.0.1") -> bool:
    """Send a bounded single ICMP echo request safely without shell=True."""
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode == 0:
        print(f"[NET] Host {host} is reachable.")
        return True
    print(f"[NET] Host {host} is unreachable.")
    return False


def check_service(service_name: str = "ssh") -> bool:
    """Check systemd unit state (exit code 0 indicates active)."""
    result = subprocess.run(
        ["systemctl", "is-active", "--quiet", service_name],
        check=False,
    )
    if result.returncode == 0:
        print(f"[SERVICE] {service_name} is RUNNING.")
        return True
    print(f"[SERVICE] {service_name} is STOPPED or FAILED.")
    return False


if __name__ == "__main__":
    print("=== Starting Ubuntu System Diagnostic ===")
    disk_ok = check_disk_usage("/")
    net_ok = check_network("8.8.8.8")
    svc_ok = check_service("ssh")
    print("=== Diagnostic Complete ===")
    sys.exit(0 if (disk_ok and net_ok and svc_ok) else 1)
