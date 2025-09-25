#!/bin/bash
TARGET=$1
echo "[*] Scanning $TARGET..."
nmap -sS -Pn -p 22,80,443,3389 -A $TARGET -oN scan_results.txt
echo "[*] Scan complete. Results saved in scan_results.txt"
