
FROM python:3.7

WORKDIR /code

COPY ./API/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./API /code/API

CMD ["uvicorn", "API.main:app", "--host", "0.0.0.0", "--port", "80"]

## curl http://localhost:8080/api/event -X POST -d '{"time": "2021-01-22T18:20:42.159246", "type": "serve", "correlation_id": "357d1bc4-3502-4592-8355-874b1c31f1a6", "site_id": "0faf8b64-a33d-4db8-aaee-aa165d13cff6"}' -H 'Content-Type: application/json'
## curl http://localhost:8080/api/report -X GET
## docker exec -it $(docker ps -qf "name=clickhouse") clickhouse client