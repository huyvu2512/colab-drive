import json
import urllib.request
from src.core.logger import log

def send_telegram(token, chat_id, message):
    if not token or not chat_id:
        return
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = json.dumps({"chat_id": chat_id, "text": message}).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                log("NOTIFY", "Đã gửi thông báo báo cáo tiến trình qua Telegram.", "NOTIFY")
    except Exception as e:
        log("WARN", f"Không thể gửi thông báo Telegram: {e}", "WARN")
