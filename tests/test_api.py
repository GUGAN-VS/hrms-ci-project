def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_leave_balance_success(client):
    response = client.post(
        "/leave-balance",
        json={
            "total_leaves": 20,
            "leaves_taken": 5
        }
    )

    assert response.status_code == 200

    assert response.json()["leave_balance"] == 15


def test_all_leaves_taken(client):
    response = client.post(
        "/leave-balance",
        json={
            "total_leaves": 10,
            "leaves_taken": 10
        }
    )

    assert response.json()["leave_balance"] == 0


def test_leaves_taken_exceeds_total(client):
    response = client.post(
        "/leave-balance",
        json={
            "total_leaves": 10,
            "leaves_taken": 15
        }
    )

    assert response.json() == {
        "error": "Leaves taken exceeds total leaves"
    }


def test_negative_leaves(client):
    response = client.post(
        "/leave-balance",
        json={
            "total_leaves": -10,
            "leaves_taken": 5
        }
    )

    assert response.status_code == 422