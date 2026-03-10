import time
import requests
import random

INGESTION_URL = "http://localhost:8000/events"


def send_event():

    event = {
        "user_id": random.randint(1, 1000),
        "event_type": random.choice(["click", "view", "purchase"]),
        "amount": random.randint(10, 5000)
    }

    try:

        response = requests.post(INGESTION_URL, json=event)

        print(f"Sent: {event} | Status: {response.status_code}")

    except Exception as e:

        print("Error sending event:", e)


def run_controller():

    print("🚀 System Controller Started")

    while True:

        send_event()

        time.sleep(1)


if __name__ == "__main__":

    run_controller()

