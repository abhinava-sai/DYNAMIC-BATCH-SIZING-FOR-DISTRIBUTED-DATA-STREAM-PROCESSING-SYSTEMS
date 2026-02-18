from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json

app = FastAPI(title="Ingestion Service")

TOPIC_NAME = "events"
KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"

producer = None

def get_producer():
    global producer
    if producer is None:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
    return producer

class Event(BaseModel):
    user_id: int
    event_type: str
    amount: float

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/events")
def publish_event(event: Event):
    producer = get_producer()
    producer.send(TOPIC_NAME, event.dict())
    producer.flush()
    return {"message": "Event sent successfully"}
