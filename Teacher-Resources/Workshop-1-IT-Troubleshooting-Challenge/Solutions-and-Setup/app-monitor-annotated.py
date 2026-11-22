#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
FILE: app-monitor-annotated.py (Instructor Annotated Version)
WORKSHOP: Workshop 1 - IT Troubleshooting Challenge (Incident 05)
STUDENT VM PATH: /opt/lab-apps/app-monitor.py (clean version without comments)
PEDAGOGICAL OBJECTIVE:
    Simulate a monitoring daemon/service that aborts startup because it is
    missing a filesystem dependency (a configuration directory and file).
    Forces students to read standard output (stdout), interpret the error
    message, and apply a minimal-impact fix without reinstalling anything.
================================================================================
"""

# [Line 1 - Shebang]: Instructs the Linux kernel that if this file is executed
# directly (./app-monitor.py) with executable permissions (+x), it must invoke
# the Python 3 interpreter located in the environment PATH (/usr/bin/env python3).

import os    # Standard library module for OS and filesystem path interactions (os.path).
import sys   # Standard library module to manage interpreter lifecycle and exit codes (sys.exit).
import time  # Standard library module to pause execution and simulate realistic load times (time.sleep).

# --- SCENARIO CONFIGURATION CONSTANTS ---
# /tmp is used because it is volatile and any unprivileged user (without sudo)
# has write permissions (rwx) to create the directory and file when solving the incident.
CONFIG_DIR = "/tmp/it-monitor"

# Absolute path that the script validates before entering its main execution loop.
# To inject the fault, the instructor must ensure this path is removed: rm -rf /tmp/it-monitor
CONFIG_FILE = f"{CONFIG_DIR}/settings.conf"


def main():
    """Main entry function encapsulating the startup and execution logic of the service."""
    
    # 1. Visual banner so students can clearly identify which binary is running
    print("========================================")
    print("   Starting IT Monitor System v1.2      ")
    print("========================================")
    
    # Intentional 1-second pause to simulate hardware/memory initialization
    time.sleep(1)
    
    # 2. Explicit diagnostic clue: prints the exact path the application is looking for
    print(f"[*] Loading configuration from {CONFIG_FILE}...")
    
    # 3. [INJECTED FAULT POINT / DEPENDENCY CHECK]
    # Checks the filesystem to see if the file (or a valid symlink) exists.
    # Instructor note: It does not validate file contents, only inode existence.
    if not os.path.exists(CONFIG_FILE):
        # Clear error messages to evaluate whether students read output before acting
        print("[-] FATAL ERROR: Configuration file not found.")
        print(f"[-] The application requires '{CONFIG_FILE}' to exist.")
        print("[-] Application terminated.")
        
        # Returns exit status 1 (Exit Status != 0), the POSIX standard indicating
        # abnormal termination/error. Useful if students check `echo $?` afterward.
        sys.exit(1)
        
    # 4. [VERIFICATION PHASE AFTER STUDENT FIX]
    # If the team created the directory (`mkdir -p /tmp/it-monitor`) and file (`touch .../settings.conf`),
    # execution flow continues past the check.
    print("[+] Configuration loaded successfully.")
    print("[+] Connecting to local services...")
    
    # Second brief pause to simulate socket/service negotiation
    time.sleep(1)
    
    # Visual confirmation of success so the Verifier/Tester can capture a screenshot as evidence
    print("[+] Application is running perfectly! (Press Ctrl+C to stop)")
    
    # 5. [CONTINUOUS EXECUTION LOOP (DAEMON SIMULATION)]
    # Keeps the process alive in the foreground so it can be inspected via `ps aux`
    # if the team opens a second terminal to verify active processes.
    try:
        while True:
            # Sleeps 2 seconds per iteration to consume ~0% CPU on the VM
            time.sleep(2)
            
    # 6. [GRACEFUL SIGNAL HANDLING (SIGINT)]
    # Catches keyboard interrupt (Ctrl+C -> SIGINT signal) to prevent Python from
    # dumping a Traceback to the terminal, which could confuse students into
    # thinking the program still has a bug.
    except KeyboardInterrupt:
        print("\n[*] Shutting down gracefully...")
        # Returns exit status 0 (Exit Status == 0), the POSIX standard for clean termination.
        sys.exit(0)


# [STANDARD PYTHON ENTRY POINT]
# Ensures main() only runs when the file is executed directly as a script
# and not if it were imported as a module from another program.
if __name__ == "__main__":
    main()
