# Challenge 2: Extending a Python Diagnostic Script with AI
**Workshop 2: AI IT Technician Assistant | Alijó IT Workshops**

---

## 1. Objective
In this challenge, you will inspect the baseline diagnostic script (`Scripts/diagnostic_script.py`) and collaborate with an AI assistant to extend its functionality safely—adding TCP port reachability checks, threshold-based disk usage warnings, and clean exit codes without introducing external third-party dependencies or destructive operations.

---

## 2. Baseline Script Inspection
Open and run the existing script in `Scripts/diagnostic_script.py`:

```bash
python3 Scripts/diagnostic_script.py
```

Review how the current script is structured:
1. It uses only the **Python standard library** (`datetime`, `os`, `platform`, `shutil`, `socket`, `subprocess`) so it runs immediately on any fresh Ubuntu server without `pip install`.
2. Every subprocess call enforces a `timeout=5` and uses read-only commands (`free -h`, `ip -br -4 addr`, `systemctl is-active`).
3. It prints a structured summary across three sections: **Storage & Memory**, **Network & DNS**, and **Core Service Status**.

---

## 3. Enhancement Requirements
Use your AI assistant to help design and integrate **three new capabilities** into `diagnostic_script.py`:

1. **TCP Port Connectivity Check (`check_tcp_port`):**
   * Use Python's built-in `socket.create_connection((host, port), timeout=3)` to verify whether local TCP ports `22` (SSH) and `80` (HTTP) are accepting connections on `127.0.0.1`.
   * Return `"OPEN"` if the connection succeeds, or `"CLOSED / FILTERED (<reason>)"` if it fails.
2. **Disk Space Threshold Alert:**
   * Update `check_disk_usage("/")` so that if disk usage exceeds **85%**, it appends a `[WARNING: HIGH DISK USAGE]` flag to the output line.
3. **JSON Export Flag (`--json`):**
   * Add a lightweight `argparse` option `--json` so administrators can output the diagnostic snapshot as valid JSON for automated monitoring pipelines while preserving the human-readable table by default.

---

## 4. Step-by-Step AI Collaboration Workflow

1. **Provide Existing Code Context:**
   * Paste `Scripts/diagnostic_script.py` into your prompt and specify the three enhancement requirements above.
   * Explicitly instruct the AI: *"Use only the Python 3 standard library. Keep all checks strictly read-only and preserve the existing 5-second timeout safeguards."*
2. **Line-by-Line Code Audit:**
   * Before running the AI-generated update, inspect every diff carefully:
     * Did it introduce `shell=True` in `subprocess.run`? *(Reject if yes—avoid shell injection risks.)*
     * Are sockets properly closed using a `with` context manager?
     * Does `--json` output valid JSON to `stdout` without extra debug banners mixed in?
3. **Test Both Output Modes:**
   ```bash
   python3 Scripts/diagnostic_script.py
   python3 Scripts/diagnostic_script.py --json | python3 -m json.tool
   ```

---

## 5. Success Criteria
* The updated `diagnostic_script.py` runs cleanly with zero third-party packages.
* TCP port checks (`22` and `80`), the `85%` disk warning logic, and the `--json` flag all work accurately and pass `python3 -m json.tool` validation.
