import os
import smtplib
import subprocess

EMAIL = os.getenv("MY_EMAIL")
EMAIL_PASS = os.getenv("MY_PASSWORD")
SIGNAL_NUMBER = os.getenv("SIGNAL_PHONE")
SIGNAL_UUID = os.getenv("SIGNAL_UUID")  # Required for signal-cli linked device


class NotificationManager:
    """Handles notifications via Signal CLI and email."""

    def send_message(self, message, to=None):
        """
        Send a Signal message.
        If 'to' is not provided, sends to self (default for personal alerts).
        """
        recipient = to or SIGNAL_NUMBER
        try:
            subprocess.run([
                "signal-cli",
                "--config", os.path.expanduser("~/.signal-cli"),
                "--username", SIGNAL_NUMBER,
                "--uuid", SIGNAL_UUID,
                "send",
                "-m", message,
                recipient
            ], check=True)
            print("✅ Signal message sent successfully.")
        except subprocess.CalledProcessError as e:
            print("❌ Failed to send Signal message.")
            print(f"Error: {e}")

    def send_email(self, message, customer_data):
        """
        Send emails to all customers in the list using SMTP.
        """
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL_PASS)

            for customer in customer_data:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=customer["email"],
                    msg=f"Subject:Flight Deal Alert!\n\n{message}".encode("utf-8")
                )
            print("📨 Email alerts sent successfully.")