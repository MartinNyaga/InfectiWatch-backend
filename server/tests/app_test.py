import pytest
from api import app, db
from flask import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_create_user(client):
    data = {
        "username": "test_user",
        "email": "test@example.com",
        "password_hash": "test_password"
    }
    response = client.post('/users', json=data, content_type='application/json')
    assert response.status_code == 201
    created_user = json.loads(response.data)
    assert created_user['username'] == data['username']

