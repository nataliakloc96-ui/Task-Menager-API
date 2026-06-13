from backend.models.user import User
from backend.core.database import SessionLocal

def test_admin_without_token(client):

    response = client.get(
        "/admin/users"
    )

    assert response.status_code == 401

def test_admin_as_user(client):

    client.post(
        "/auth/register",
        json={
            "email": "normal@test.com",
            "password": "test123"
        }
    )

    login = client.post(
        "/auth/login",
        data={
            "username": "normal@test.com",
            "password": "test123"
        }
    )

    token = login.json()["access_token"]

    response = client.get(
        "/admin/users",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 403

def test_admin_as_admin(client):

    email = "admin@test.com"

    client.post(
        "/auth/register",
        json={
            "email": email,
            "password": "test123"
        }
    )

    db = SessionLocal()

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    user.role = "admin"

    db.commit()
    db.close()

    login = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "test123"
        }
    )

    token = login.json()["access_token"]

    response = client.get(
        "/admin/users",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert isinstance(
        response.json(),
        list
    )