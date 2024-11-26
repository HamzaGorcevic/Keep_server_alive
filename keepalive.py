import argparse
import os
import threading
import time
from flask import Flask
import requests

# Flask server setup
app = Flask(__name__)

@app.route("/")
def home():
    return "Keep-Alive Service is Running", 200

# Keep-Alive ping logic
def keep_alive():
    URL = "https://pyzzlebackend.onrender.com/game/alive" 
    PING_INTERVAL = 300  # 5 minutes

    while True:
        try:
            response = requests.get(URL)
            print(f"Pinged {URL}: Status {response.status_code}")
        except requests.RequestException as e:
            print(f"Error pinging {URL}: {e}")
        time.sleep(PING_INTERVAL)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Keep-Alive Service")
    parser.add_argument("address", nargs="?", default="0.0.0.0:5000", help="Address and port to bind to (e.g., 0.0.0.0:8000)")
    args = parser.parse_args()

    # Extract host and port from the address
    address, port = args.address.split(":")
    port = int(port)

    # Start the keep-alive thread
    threading.Thread(target=keep_alive, daemon=True).start()

    # Run Flask server
    app.run(host=address, port=port)
