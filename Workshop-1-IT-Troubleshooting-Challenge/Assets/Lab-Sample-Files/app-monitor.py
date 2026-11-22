#!/usr/bin/env python3
import os
import sys
import time

CONFIG_DIR = "/tmp/it-monitor"
CONFIG_FILE = f"{CONFIG_DIR}/settings.conf"

def main():
    print("========================================")
    print("   Starting IT Monitor System v1.2      ")
    print("========================================")
    time.sleep(1)
    
    print(f"[*] Loading configuration from {CONFIG_FILE}...")
    
    if not os.path.exists(CONFIG_FILE):
        print("[-] FATAL ERROR: Configuration file not found.")
        print(f"[-] The application requires '{CONFIG_FILE}' to exist.")
        print("[-] Application terminated.")
        sys.exit(1)
        
    print("[+] Configuration loaded successfully.")
    print("[+] Connecting to local services...")
    time.sleep(1)
    print("[+] Application is running perfectly! (Press Ctrl+C to stop)")
    
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[*] Shutting down gracefully...")
        sys.exit(0)

if __name__ == "__main__":
    main()
