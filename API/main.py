from multiprocessing import Event
import json
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
import pandas as pd
from typing import Optional

from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

from API.DAO import SqlConnector

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

@app.post("/api/event")
def rank(payload: EventPayload):
    try:
        producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        producer.send('event', jsonable_encoder(payload))
        producer.flush()

        return {'message':'success'}
    except NoBrokersAvailable:
        raise HTTPException(status_code=500, detail="Could not find a Kafka")
    except:
        raise HTTPException(status_code=500, detail="Something went Wrong")

@app.get("/api/report")
def report(site_id: Optional[str] = None):
    try:
        where_condition =""
        if site_id:
            where_condition = "where site_id = '{}'".format(site_id)
        sql =  '''
                select
                    toDate(parseDateTimeBestEffort(time)) as day,
                    site_id,
                    type,
                    count(distinct correlation_id) as count
                from eventdb.event
                {}
                group by toDate(parseDateTimeBestEffort(time)), site_id, type
                '''.format(where_condition)

        with SqlConnector() as con:
            query_result = con.execute(sql)

        if query_result:
            df = pd.DataFrame(query_result)
            df.columns = ['time','site_id','type','count']
            reshaped_result = df.pivot(index=['time','site_id'],columns='type',values='count').reset_index().to_dict(orient='records')
            return {'counters': reshaped_result}
        else:
            return {'counters': []}
    except:
        raise HTTPException(status_code=500, detail="Something went Wrong")