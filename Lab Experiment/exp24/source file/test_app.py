from app import app

client = app.test_client()

def test_home():
    r = client.get("/")
    assert r.status_code == 200
    assert r.get_json()["status"] == "running"

def test_add():
    r = client.get("/add/2/3")
    assert r.get_json()["result"] == 5
