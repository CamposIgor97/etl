from kafka import KafkaProducer
import uuid
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for _ in range(10):
    producer.send('foobar', {"id": str(uuid.uuid4())})
    producer.flush()


#names = ['john','pablo','andrew','andreas','rodrigo']
#lastnames = ['silva','pirovich', 'usok', 'matias']
#credits = [1000,2512,6521,125,1478,1259]
     #str.encode(json.dumps({
     #     "name": random.choice(names),
     #     "lastname": random.choice(lastnames),
     #     "credits": random.choice(credits)
     #     })))
