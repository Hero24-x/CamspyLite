# core/scan.py
import requests

SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
SHODAN_URL = "https://api.shodan.io/shodan/host/search"

def scan_cameras(query="webcamXP"):
    params = {
        "key": SHODAN_API_KEY,
        "query": query
    }
    response = requests.get(SHODAN_URL, params=params)
    data = response.json()
    results = []

    for match in data.get("matches", []):
        ip = match.get("ip_str")
        port = match.get("port")
        if ip and port:
            results.append(f"http://{ip}:{port}")

    return results
