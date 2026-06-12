from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_register(client):
    response = client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test123"
    })

    assert response.status_code in [200, 409]
    if response.status_code == 200:
        assert "id" in response.json()

def test_login(client):
    register = client.post(
        "/auth/register",
        json={
            "email": "login@test.com",
            "password": "test123"
        }
    )

    print(register.status_code)
    print(register.json())

    response = client.post("/auth/login", data={
        "username": "login@test.com",
        "password": "test123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

def test_refresh_flow(client):

    client.post(
        "/auth/register",
        json={
            "email": "refresh@test.com",
            "password": "test123"
        }
    )

    login = client.post(
        "/auth/login",
        data={
            "username": "refresh@test.com",
            "password": "test123"
        }
    )

    refresh_token = login.json()["refresh_token"]

    response = client.post(
        "/auth/refresh",
        json={
            "refresh_token": refresh_token
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_wrong_password(client):

    response = client.post(
        "/auth/login",
        data={
            "username": "login@test.com",
            "password": "wrong"
        }
    )

    assert response.status_code in [400, 401]