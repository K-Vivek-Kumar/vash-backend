def test_projects(client):
    response = client.get("/products")
    assert response.status_code == 200

    json_data = response.json
    assert "products" in json_data

    products_list = json_data["products"]
    assert len(products_list) <= 10


def test_projects_with_query(client):
    response = client.get("/products?q={'dfsfkdsklhfdssdkld'}")
    assert response.status_code == 200

    json_data = response.json
    assert "products" in json_data

    products_list = json_data["products"]
    assert len(products_list) == 0
