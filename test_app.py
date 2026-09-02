import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Verifica que la ruta principal responda 200 OK"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_response_json(client):
    """Verifica que el contenido del JSON sea correcto"""
    response = client.get('/')
    json_data = response.get_json()
    assert json_data["status"] == "success"

def test_health_check(client):
    """Verifica la ruta de health check"""
    response = client.get('/health')
    assert response.status_code == 200
