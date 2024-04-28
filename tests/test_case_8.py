from project import create_app


def test_retailer_login(client):
    app = create_app()
    with app.test_client() as client:
        response = client.post(
            "/retailer-login",
            json={"email": "vash4@ret.in", "password": "vash1"},
        )
        assert response.status_code != 200
        assert b"Incorrect Password" in response.data


def test_retailer_login_without_password(client):
    app = create_app()
    with app.test_client() as client:
        response = client.post(
            "/retailer-login",
            json={"email": "vash4@ret.in"},
        )
        assert response.status_code != 200


def test_retailer_login_without_email(client):
    app = create_app()
    with app.test_client() as client:
        response = client.post(
            "/retailer-login",
            json={"password": "vash1"},
        )
        assert response.status_code != 200
