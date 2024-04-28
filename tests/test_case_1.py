import json
from project import create_app

acc = ""


def test_retailer_login(client):
    global acc
    app = create_app()
    with app.test_client() as client:
        response = client.post(
            "/retailer-login",
            json={"email": "vash4@ret.in", "password": "vash"},
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "access_token" in data
        assert isinstance(data["access_token"], str)
        acc = data["access_token"]
    print("Successful")


def test_product_upload(client):
    global acc
    product_data = {
        "name": "Test Product 3",
        "quantity": 10,
        "category": "Electronics",
        "subCategory": "Smartphones",
        "company": "Test Company",
        "description": "Test description",
        "price": 999.99,
        "discount": 10,
    }
    response = client.post(
        "/product-upload",
        json=product_data,
        headers={"Authorization": "Bearer " + acc},
    )
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Product Uploaded"
