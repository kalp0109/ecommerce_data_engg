import json
import time
import random
from kafka import KafkaProducer
from datetime import datetime,timezone
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

BOOTSTRAP_SERVER = os.getenv("CONFLUENT_BOOTSTRAP_SERVER")
API_KEY = os.getenv("CONFLUENT_API_KEY")
API_SECRET = os.getenv("CONFLUENT_API_SECRET")
# kafka configuration

TOPIC = 'ORDER_TOPICS'


# CREATE kafka producer
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVER,
    security_protocol="SASL_SSL",
    sasl_mechanism="PLAIN",
    sasl_plain_username= API_KEY,
    sasl_plain_password= API_SECRET,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Sample master data
customers = [
    "CUST00001",
    "CUST00002",
    "CUST00003",
    "CUST00004",
    "CUST00005"
]

products = [
    ("PROD00001", 1500.00),
    ("PROD00002", 2500.00),
    ("PROD00003", 3500.00),
    ("PROD00004", 4500.00),
    ("PROD00005", 5500.00)
]

statuses = [
    "Shipped",
    "Delivered",
    "Cancelled"
]

print('Starting Order Producer.....')
print(f'sending events to topic: {TOPIC}')

try:
    while True:
        product_id, unit_price = random.choice(products)
        order_event = {
                "event_id": str(uuid.uuid4()),
                "event_ts": datetime.now(timezone.utc).isoformat(),

                "order_id": f"ORD{random.randint(10000, 99999)}",

                "customer_id": random.choice(customers),

                "product_id": product_id,

                "quantity": random.randint(1, 5),

                "unit_price": unit_price,

                "status": random.choice(statuses)
            }

        # Send event to Kafka
        producer.send(TOPIC, value=order_event)

        # Make sure event is sent
        producer.flush()
        print("Sent:", order_event)

            # Wait before generating next event
        time.sleep(2)

except KeyboardInterrupt:

    print("\nStopping producer...")


finally:

    producer.close()