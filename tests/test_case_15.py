def test_presentpages(client):
    response = client.get("/admin-statistics/4")
    assert response.status_code == 404


def test_presentproducts(client):
    response = client.get("/products/abc")
    assert response.status_code == 404
