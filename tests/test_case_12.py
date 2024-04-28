import pytest


def test_projects_with_query_with_verification(client):
    response = client.get("/products?page=2&q=Geology")
    assert response.status_code == 200

    json_data = response.json
    assert "products" in json_data

    products_list = json_data["products"]
    yes = False
    for product in products_list:
        b = product["name"] == "Geology"
        yes = yes or b
    assert yes == False
    assert len(products_list) <= 10


@pytest.mark.benchmark(group="products")
def test_products_response_time(client, benchmark):
    response = benchmark(client.get, "/products?page=2&q=Geology")
    assert response.status_code == 200
    assert benchmark.stats["mean"] < 1.0


@pytest.mark.benchmark(group="products")
def test_products_response_time_page_crossed(client, benchmark):
    response = benchmark(client.get, "/products?page=100&q=Geology")
    assert response.status_code == 200
    assert benchmark.stats["mean"] < 1.0


@pytest.mark.benchmark(group="products")
def test_products_response_time_no_result(client, benchmark):
    response = benchmark(client.get, "/products?page=2&q=Geologyicsalnasas")
    assert response.status_code == 200
    assert benchmark.stats["mean"] < 1.0
