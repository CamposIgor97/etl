from multiprocessing import Event
import json
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from clickhouse_driver import Client

from kafka import KafkaProducer


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

class EventPayload(BaseModel):
    time: str
    type: str
    correlation_id: str
    site_id:str

@app.post("/event")
def rank(payload: EventPayload):
    print(payload)

    #project_id = payload.panelist_id
    #if not project_id:
    #    raise HTTPException(status_code=400, detail="Missing project_id")

    try:
        producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        producer.send('event', jsonable_encoder(payload))
        producer.flush()

        return {'message':'success'}

    except Exception as e:
        print(e)
        return {'message':e}

@app.get("/report")
def report():
    client = Client(host='some-clickhouse-server')
    result = client.execute('SELECT * FROM eventdb.event')
    return {'message': result}
    