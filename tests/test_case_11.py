def test_user_signup(client):
    signup_data = {
        "email": "test@example.com",
        "password": "password123",
    }
    response = client.post("/signup", json=signup_data)
    assert response.status_code != 200


def test_retailer_signup(client):
    retailer_signup_data = {
        "name": "Test Retailer",
        "email": "retailer@example.com",
        "password": "password123",
        "address": "123 Test Street",
    }
    response = client.post("/retailer-signup", json=retailer_signup_data)
    assert response.status_code != 200
