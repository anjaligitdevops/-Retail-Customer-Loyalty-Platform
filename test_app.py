from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "running"


def test_loyalty():
    client = app.test_client()
    response = client.get("/loyalty")
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["customer"] == "Anjali"
    assert data["loyalty_points"] == 250


def test_promotions():
    client = app.test_client()
    response = client.get("/promotions")
    
    assert response.status_code == 200
    data = response.get_json()
    assert len(data["promotions"]) == 2
    assert data["promotions"][0]["title"] == "Summer Sale"
