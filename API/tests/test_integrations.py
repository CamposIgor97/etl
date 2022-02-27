from fastapi.testclient import TestClient
from copy import deepcopy

from ..main import app

client = TestClient(app)


def test_read_report():
    response = client.get("/api/report")
    assert response.status_code == 200
    assert response.json() == {"counters":[{"time":"2021-01-22","site_id":"0faf8b64-a33d-4db8-aaee-aa165d13cff6","serve":4,"solve":3}]}

def test_read_report_with_invalid_site_id():
    response = client.get("/api/report?site_id=HERE_IM_PUTTING_A_INVALID_VALUE")
    assert response.status_code == 200
    assert response.json() == {"counters":[]}

def test_insert_event():
    response = client.post(
        "/api/event",
        json={"time": "2021-01-22T18:20:42.159246", "type": "serve", "correlation_id": "357d1bc4-3502-4592-8355-874b1c31f1a6", "site_id": "0faf8b64-a33d-4db8-aaee-aa165d13cff6"},
    )
    assert response.status_code == 200
    assert response.json() == {'message':'success'}

def test_insert_event_missing_fields():
    payload = {"time": "2021-01-22T18:20:42.159246", "type": "serve", "correlation_id": "357d1bc4-3502-4592-8355-874b1c31f1a6", "site_id": "0faf8b64-a33d-4db8-aaee-aa165d13cff6"}

    for key in payload.keys():
        payload_missing_key = deepcopy(payload)
        payload_missing_key.pop(key, None)
        response = client.post(
            "/api/event",
            json=payload_missing_key,
        )
        assert response.status_code == 422
        #assert response.json() == {'message':'success'}
