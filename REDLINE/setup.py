import os
from colorama import Fore

def setup_main():
    print(f"""{Fore.LIGHTRED_EX}
███████╗███████╗████████╗██╗   ██╗██████╗ 
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
███████╗█████╗     ██║   ██║   ██║██████╔╝
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
███████║███████╗   ██║   ╚██████╔╝██║     
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
         {Fore.RESET}""")
    
    os.system("pip install pynput --break-system-packages")
    os.system("pip install pillow --break-system-packages")

if __name__ == "__main__":
    setup_main()

