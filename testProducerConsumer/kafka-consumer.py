from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('event',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    consumer_timeout_ms=1000,
    value_deserializer = json.loads)

for msg in consumer:
    print(msg.value)