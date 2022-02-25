from multiprocessing import Event
import urllib3
import json
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

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

    #producer = KafkaProducer(
    #    bootstrap_servers=['localhost:9093'],
    #    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    #producer.send('foobar', payload)
    #producer.flush()

    return 'sucesso'