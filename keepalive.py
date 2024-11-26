from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import requests

app = Flask(__name__)

def ping_service():
    print("ping_service called!")
    try:
        response = requests.get("https://pyzzlebackend.onrender.com/game/alive")
        print(f"Pinged: Status {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(func=ping_service, trigger="interval", seconds = 250)
scheduler.start()
print("Scheduler has started!")

@app.route('/')
def index():
    return "Keep-Alive Service is Running!"

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host="0.0.0.0", port=5000, debug=True)
