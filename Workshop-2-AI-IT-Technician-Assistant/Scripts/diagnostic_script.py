#!/usr/bin/env python3
"""
System & Network Diagnostic Baseline Script
Workshop 2: AI IT Technician Assistant | Alijó IT Workshops

Collects read-only host health, disk, memory, network interface, DNS,
and key systemd service statuses into a clean summary report.
"""

from datetime import datetime
import os
import platform
import shutil
import socket
import subprocess


def run_cmd(cmd: list[str]) -> str:
    """Execute a safe, read-only system command and return trimmed output."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        output = result.stdout.strip() or result.stderr.strip()
        return output if output else "No output"
    except FileNotFoundError:
        return f"Command not found: {cmd[0]}"
    except subprocess.TimeoutExpired:
        return f"Command timed out: {' '.join(cmd)}"
    except Exception as exc:  # pylint: disable=broad-except
        return f"Error: {exc}"


def check_disk_usage(path: str = "/") -> str:
    """Return human-readable disk usage for the given mount point."""
    total, used, free = shutil.disk_usage(path)
    gb = 1024 ** 3
    pct = (used / total) * 100 if total else 0.0
    return (
        f"Mount {path}: {used / gb:.1f} GB used / {total / gb:.1f} GB total "
        f"({pct:.1f}% used, {free / gb:.1f} GB free)"
    )


def check_dns(hostname: str = "example.com") -> str:
    """Verify basic DNS resolution."""
    try:
        ip_addr = socket.gethostbyname(hostname)
        return f"OK ({hostname} -> {ip_addr})"
    except socket.gaierror as exc:
        return f"FAILED ({hostname}: {exc})"


def check_service(service_name: str) -> str:
    """Check systemd unit active state on Linux systems."""
    if platform.system() != "Linux":
        return "Skipped (non-Linux host)"
    return run_cmd(["systemctl", "is-active", service_name])


def main() -> None:
    """Generate the diagnostic summary report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    os_info = f"{platform.system()} {platform.release()} ({platform.machine()})"

    print("=" * 64)
    print("ALIJÓ IT WORKSHOPS — SYSTEM DIAGNOSTIC SNAPSHOT")
    print("=" * 64)
    print(f"Timestamp : {timestamp}")
    print(f"Hostname  : {hostname}")
    print(f"OS Kernel : {os_info}")
    print(f"User      : {os.getenv('USER', 'unknown')}")
    print("-" * 64)

    print("\n[1] STORAGE & MEMORY")
    print(check_disk_usage("/"))
    if platform.system() == "Linux":
        print(run_cmd(["free", "-h"]))

    print("\n[2] NETWORK & DNS")
    if platform.system() == "Linux":
        print(run_cmd(["ip", "-br", "-4", "addr"]))
    print(f"DNS Lookup: {check_dns('example.com')}")

    print("\n[3] CORE SERVICE STATUS")
    for svc in ("ssh", "apache2", "ufw"):
        print(f"- {svc:<10}: {check_service(svc)}")

    print("\n" + "=" * 64)
    print("Diagnostic collection complete (read-only mode).")
    print("=" * 64)


if __name__ == "__main__":
    main()
