import socket
import time
import requests
from datetime import datetime

while True:
    try:
        ip = socket.gethostbyname("google.com")

        r = requests.get("https://google.com", timeout=10)

        msg = f"""
TIME: {datetime.now()}
DNS: OK -> {ip}
GOOGLE: {r.status_code}
"""

        print(msg)

        with open("status.txt", "w") as f:
            f.write(msg)

    except Exception as e:
        err = f"ERROR: {e}"
        print(err)

        with open("status.txt", "w") as f:
            f.write(err)

    time.sleep(60)
