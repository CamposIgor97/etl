from kafka import KafkaConsumer
consumer = KafkaConsumer('foobor')
for msg in consumer:
     print(msg.value)