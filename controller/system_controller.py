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
        response = requests.post(INGESTION_URL, json=event, timeout=2)
        print(f"Sent: {event} | Status: {response.status_code}")
    except Exception as e:
        print(f"Ingestion service unreachable. Retrying... Error: {e}")


def main():
    print("System Controller Started...")
    while True:
        send_event()
        time.sleep(2)


if __name__ == "__main__":
    main()