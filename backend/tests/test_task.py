from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def get_token(client):
    register = client.post("/auth/register", json={
        "email": "task@test.com",
        "password": "test123"
    })

    print("REGISTER")
    print(register.status_code)
    print(register.json())

    response = client.post("/auth/login", data={
        "username": "task@test.com",
        "password": "test123"
    })

    print("RESPONSE")
    print(response.status_code)
    print(response.json())

    return response.json()["access_token"]

def test_create_task(client):
    token = get_token(client)

    response = client.post(
        "/tasks/",
        json={
            "title": "Test task",
            "priority": "high"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Test task"

def test_get_tasks(client):
    token = get_token(client)

    response = client.get(
        "/tasks/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_task_filtering(client):
    token = get_token(client)

    response = client.get(
        "/tasks/?search=Test",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

def test_update_task(client):

    token = get_token(client)

    create = client.post(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Old title"
        }
    )

    task_id = create.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "New title"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "New title"

def test_delete_task(client):

    token = get_token(client)

    create = client.post(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Delete me"
        }
    )

    task_id = create.json()["id"]

    response = client.delete(
        f"/tasks/{task_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200