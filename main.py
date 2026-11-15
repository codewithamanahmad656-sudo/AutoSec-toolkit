import sys
import time
import os

# Terminal colors for cool hacker vibe
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Colors.GREEN}{Colors.BOLD}
    ========================================
       🚀 AutoSec-Toolkit | 1-Click Wrapper   
       Designed for TryHackMe & CTF Labs    
    ========================================
    {Colors.ENDC}""")

def main():
    banner()
    
    # Disclaimer Check
    print(f"{Colors.WARNING}[!] DISCLAIMER: This tool is strictly for educational purposes and authorized CTF labs.{Colors.ENDC}")
    consent = input(f"{Colors.BOLD}Do you agree to use this ethically? (y/n): {Colors.ENDC}").strip().lower()
    
    if consent != 'y':
        print(f"{Colors.FAIL}[-] Exiting. Stay ethical!{Colors.ENDC}")
        sys.exit()

    banner()
    print(f"{Colors.BLUE}[*] Initializing Automation Module...{Colors.ENDC}\n")
    
    # User Inputs
    target = input(f"{Colors.BOLD}Enter Target IP / URL: {Colors.ENDC}").strip()
    port = input(f"{Colors.BOLD}Enter Port (e.g., 80/443): {Colors.ENDC}").strip()
    
    if not target or not port:
        print(f"{Colors.FAIL}[!] Target and Port cannot be empty!{Colors.ENDC}")
        sys.exit()

    print(f"\n{Colors.GREEN}[+] Target locked: {target}:{port}{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Running automated diagnostics & payload sequence...{Colors.ENDC}\n")
    
    # Simulating automated process (Yahan tum apna main hacking/recon logic daloge)
    for i in range(1, 4):
        print(f"[{i}/3] Executing automated pipeline step...")
        time.sleep(1)
        
    print(f"\n{Colors.GREEN}{Colors.BOLD}[✔] Process completed successfully! Check logs for output.{Colors.ENDC}")

if __name__ == "__main__":
    main()