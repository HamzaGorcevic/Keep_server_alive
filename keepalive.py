import time
import requests

URL = "https://pyzzlebackend.onrender.com/game/alive" 
PING_INTERVAL = 30

def ping_service():
    try:
        response = requests.get(URL)
        print(f"Pinged {URL}: Status {response.status_code}")
    except requests.RequestException as e:
        print(f"Error pinging {URL}: {e}")

def main():
    print(f"Starting Keep-Alive Service for {URL}")
    while True:
        ping_service()
        time.sleep(PING_INTERVAL)

if __name__ == "__main__":
    main()
