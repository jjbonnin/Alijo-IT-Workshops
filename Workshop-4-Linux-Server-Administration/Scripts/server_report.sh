#!/usr/bin/env bash
# ==============================================================================
# Server Health & Security Baseline Report
# Workshop 4: Linux Server Administration | Alijó IT Workshops
# ==============================================================================

set -u

REPORT_DATE="$(date '+%Y-%m-%d %H:%M:%S')"
HOSTNAME_STR="$(hostname)"
KERNEL_STR="$(uname -sr)"
UPTIME_STR="$(uptime -p)"

echo "========================================================================"
echo "ALIJÓ IT WORKSHOPS — LINUX SERVER HEALTH REPORT"
echo "========================================================================"
echo "Generated : ${REPORT_DATE}"
echo "Hostname  : ${HOSTNAME_STR}"
echo "Kernel    : ${KERNEL_STR}"
echo "Uptime    : ${UPTIME_STR}"
echo "------------------------------------------------------------------------"

echo ""
echo "[1] CPU LOAD & MEMORY USAGE"
uptime
free -h

echo ""
echo "[2] ROOT FILESYSTEM DISK USAGE"
df -h /

echo ""
echo "[3] NETWORK INTERFACES & DEFAULT ROUTE"
ip -br -4 addr
ip route | grep '^default' || echo "No default route configured"

echo ""
echo "[4] CORE SYSTEMD SERVICES"
for svc in ssh apache2 ufw; do
    if systemctl list-unit-files "${svc}.service" >/dev/null 2>&1; then
        state="$(systemctl is-active "${svc}" 2>/dev/null || true)"
        enabled="$(systemctl is-enabled "${svc}" 2>/dev/null || true)"
        printf "  %-12s : active=%-10s enabled=%s\n" "${svc}" "${state}" "${enabled}"
    else
        printf "  %-12s : not installed\n" "${svc}"
    fi
done

echo ""
echo "[5] LISTENING TCP/UDP PORTS"
ss -tulpn

echo ""
echo "[6] RECENT AUTHENTICATION FAILURES (LAST 5)"
if [ -r /var/log/auth.log ]; then
    grep -i "Failed password" /var/log/auth.log | tail -n 5 || echo "  No failed password entries found."
else
    echo "  /var/log/auth.log not readable (run with sudo for auth log inspection)."
fi

echo ""
echo "========================================================================"
echo "Report complete."
echo "========================================================================"
