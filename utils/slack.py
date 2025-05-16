import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_slack_message(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("⚠️ No SLACK_WEBHOOK_URL set in .env")
        return

    payload = {"text": message}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code != 200:
            print("Slack error:", response.text)
    except Exception as e:
        print("Slack exception:", str(e))
