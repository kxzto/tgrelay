import socket
import time
import requests

while True:
    try:
        ip = socket.gethostbyname("google.com")
        print(f"DNS OK -> {ip}")

        r = requests.get("https://google.com", timeout=10)

        print(f"Google status -> {r.status_code}")

    except Exception as e:
        print("ERROR:", e)

    time.sleep(60)
