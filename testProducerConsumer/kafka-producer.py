from kafka import KafkaProducer
import uuid
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9093'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for _ in range(10):
    producer.send('foobar', {"time": "2021-01-22T18:20:42.159246", "type": "serve", "correlation_id": "357d1bc4-3502-4592-8355-874b1c31f1a6", "site_id": "0faf8b64-a33d-4db8-aaee-aa165d13cff6"})
    producer.flush()


#names = ['john','pablo','andrew','andreas','rodrigo']
#lastnames = ['silva','pirovich', 'usok', 'matias']
#credits = [1000,2512,6521,125,1478,1259]
     #str.encode(json.dumps({
     #     "name": random.choice(names),
     #     "lastname": random.choice(lastnames),
     #     "credits": random.choice(credits)
     #     })))
