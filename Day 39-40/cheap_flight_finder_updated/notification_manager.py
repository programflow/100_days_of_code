# notification_manager.py

import subprocess
import os
from dotenv import load_dotenv
import smtplib
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.signal_cli_path = "/home/kevinfloort/signal-cli-0.13.14/bin/signal-cli"  # Update if needed
        self.sender = os.environ["SIGNAL_SENDER"]
        self.recipient = os.environ["SIGNAL_RECIPIENT"]

    def send_message(self, message: str):
        try:
            subprocess.run([
                self.signal_cli_path,
                "-u", self.sender,
                "send",
                self.recipient,
                "-m", message
            ], check=True)
            print("✅ Signal message sent.")
        except subprocess.CalledProcessError as e:
            print("❌ Failed to send message.")
            print(e)

    def send_email(self, message, customers):
        for customer in customers:

            my_email = os.getenv("MY_EMAIL")
            password = os.getenv("EMAIL_PASS")
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=customer["whatIsYourEmail"],
                msg=message
            )
            connection.close()