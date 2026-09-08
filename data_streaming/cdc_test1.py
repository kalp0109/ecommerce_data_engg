import json
import time
from kafka import KafkaProducer
from datetime import datetime, timezone
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

BOOTSTRAP_SERVER = os.getenv("CONFLUENT_BOOTSTRAP_SERVER")
API_KEY = os.getenv("CONFLUENT_API_KEY")
API_SECRET = os.getenv("CONFLUENT_API_SECRET")

TOPIC = "ORDER_TOPICS"

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVER,
    security_protocol="SASL_SSL",
    sasl_mechanism="PLAIN",
    sasl_plain_username=API_KEY,
    sasl_plain_password=API_SECRET,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

order_id = "ORD999999"

# -------------------------
# INSERT event
# -------------------------

insert_event = {
    "event_id": str(uuid.uuid4()),
    "event_ts": datetime.now(timezone.utc).isoformat(),
    "order_id": order_id,
    "customer_id": "CUST00001",
    "product_id": "PROD00001",
    "quantity": 2,
    "unit_price": 1500.00,
    "status": "Shipped",
    "operation": "I"
}

producer.send(TOPIC, value=insert_event)
producer.flush()

print("Sent INSERT:", insert_event)

time.sleep(3)

# -------------------------
# UPDATE event
# -------------------------

update_event = {
    "event_id": str(uuid.uuid4()),
    "event_ts": datetime.now(timezone.utc).isoformat(),
    "order_id": order_id,
    "customer_id": "CUST00001",
    "product_id": "PROD00001",
    "quantity": 3,
    "unit_price": 1500.00,
    "status": "Delivered",
    "operation": "U"
}

producer.send(TOPIC, value=update_event)
producer.flush()

print("Sent UPDATE:", update_event)

producer.close()