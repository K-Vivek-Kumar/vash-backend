import json
from project import create_app

acc = ""


def test_user_login(client):
    global acc
    app = create_app()
    with app.test_client() as client:
        response = client.post(
            "/login",
            json={"email": "vash1@ret.in", "password": "vash"},
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "access_token" in data
        assert isinstance(data["access_token"], str)
        acc = data["access_token"]
    print("Successful")


def test_cart_upload(client):
    global acc
    cart_data = {"product_id": 3, "quantity": 2}
    response = client.post(
        "/upload-cart", json=cart_data, headers={"Authorization": "Bearer " + acc}
    )
    assert response.status_code == 200
