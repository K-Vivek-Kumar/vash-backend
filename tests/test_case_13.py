import json
import pytest

from project import create_app

acc = ""


def test_retailer_login(client):
    global acc
    app = create_app()
    with app.test_client() as client:
        response = client.post(
            "/admin-login",
            json={"email": "vash@admin.in", "password": "vash"},
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "access_token" in data
        assert isinstance(data["access_token"], str)
        acc = data["access_token"]
    print("Successful")


@pytest.mark.benchmark(group="admin_stats")
def test_admin_stats_response_time(client, benchmark):
    global acc
    headers = {"Authorization": f"Bearer {acc}"}
    response = benchmark(client.get, "/admin-stats", headers=headers)
    assert response.status_code == 200
    assert benchmark.stats["mean"] < 5000
