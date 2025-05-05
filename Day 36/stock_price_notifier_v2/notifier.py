
import os
import smtplib
import subprocess
import unicodedata
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_PHONE = os.getenv("MY_PHONE")
SIGNAL_UUID = os.getenv("SIGNAL_UUID")
CARRIER = os.getenv("CARRIER", "spectrum")

CARRIERS = {
    "spectrum": "@mypixmessages.com",
    "verizon": "@vtext.com",
    "tmobile": "@tmomail.net",
}

def clean_text(text, limit=100):
    safe = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return " ".join(safe.strip().split())[:limit]

def send_sms_via_email(message: str):
    recipient = MY_PHONE + CARRIERS.get(CARRIER, "")
    msg = EmailMessage()
    msg["From"] = MY_EMAIL
    msg["To"] = recipient
    msg.set_content(message, charset="utf-8")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(MY_EMAIL, MY_PASSWORD)
        server.send_message(msg)

def send_via_signal(message: str):
    command = ["signal-cli", "-u", SIGNAL_UUID, "send", "-m", message, MY_PHONE]
    subprocess.run(command, capture_output=True, text=True)

def notify_all(message: str, use_signal=True):
    print(f"Sending notification: {message[:40]}...")
    if use_signal:
        send_via_signal(message)
    else:
        send_sms_via_email(clean_text(message))
