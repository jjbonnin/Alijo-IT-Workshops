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
