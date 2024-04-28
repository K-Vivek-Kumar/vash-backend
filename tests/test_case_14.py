def test_admin_route_without_token(client):
    response = client.get("/admin-stats")
    assert response.status_code == 401


def test_pending_orders_without_token(client):
    response = client.get("/pending-orders")
    assert response.status_code == 401


def test_user_profile_without_token(client):
    response = client.get("/user-profile")
    assert response.status_code == 401


def test_current_retailer_without_token(client):
    response = client.get("/current-retailer")
    assert response.status_code == 401


def test_current_user_without_token(client):
    response = client.get("/current-user")
    assert response.status_code == 401


def test_admin_home_without_token(client):
    response = client.get("/admin-home")
    assert response.status_code == 401


def test_cart_without_token(client):
    response = client.get("/cart")
    assert response.status_code == 401
