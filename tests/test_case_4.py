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
    print("Login successful")


def test_upload_existing_cart_item(client):
    global acc

    # Retrieve existing cart items
    response = client.get("/cart", headers={"Authorization": "Bearer " + acc})
    assert response.status_code == 200
    cart_data = json.loads(response.data)

    assert "Items" in cart_data
    items = cart_data["Items"]

    if items:
        item_to_update = items[0]

        updated_quantity = item_to_update["quantity"] + 1
        cart_data = {"product_id": item_to_update["id"], "quantity": 1}
        response = client.post(
            "/upload-cart", json=cart_data, headers={"Authorization": "Bearer " + acc}
        )
        assert response.status_code == 200

        response = client.get("/cart", headers={"Authorization": "Bearer " + acc})
        assert response.status_code == 200
        updated_cart_data = json.loads(response.data)

        assert "Items" in updated_cart_data
        updated_items = updated_cart_data["Items"]
        updated_item = next(
            (item for item in updated_items if item["id"] == item_to_update["id"]), None
        )
        assert updated_item is not None
        assert updated_item["quantity"] == updated_quantity

    else:
        print("Cart is empty, cannot perform cart operations.")
