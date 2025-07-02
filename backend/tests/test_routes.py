from fastapi.testclient import TestClient

from main import app
from modules.calcul import square

client = TestClient(app)

def test_home_route():
    response = client.get('/api/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, world!'}

def test_health_route():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json() == {'message': 'The server is up and running!'}

def test_calcul_route_with_integer():
    input = 2
    response = client.post('/api/calcul', json={"integer": input})
    assert response.status_code == 200
    assert response.json() == {'result': square(input)}

def test_calcul_route_with_float():
    input = 2.5
    response = client.post('/api/calcul', json={"integer": input})
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "int_from_float"
