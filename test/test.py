from starlette.testclient import TestClient # type: ignore
from app.db import database
from app.main import app

client = TestClient(app)

stores = database.generate_store_db()

def test_get_stores():
    response = client.get('/stores')
    assert response.status_code == 200
    assert response.json() == stores

def test_get_store():
    response = client.get('/stores/1')
    assert response.status_code == 200
    assert response.json() == stores[0]

def test_add_store():
    body = {"name": "My Test Store", "address": "My test address"}
    response = client.post('/stores', json=body)
    assert response.status_code == 201

def test_delete_store():
    response = client.delete('/stores/1')
    assert response.status_code == 201