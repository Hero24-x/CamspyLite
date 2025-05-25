# core/stream_checker.py
import requests
import os
from datetime import datetime

def try_snapshot(url):
    try:
        snapshot_url = f"{url}/snapshot.jpg"  # common endpoint
        response = requests.get(snapshot_url, timeout=5)
        if response.status_code == 200:
            if not os.path.exists("snapshots"):
                os.makedirs("snapshots")
            filename = f"snapshots/{url.replace('http://', '').replace(':', '_')}_{datetime.now().strftime('%H%M%S')}.jpg"
            with open(filename, "wb") as f:
                f.write(response.content)
            return filename
    except:
        pass
    return None
