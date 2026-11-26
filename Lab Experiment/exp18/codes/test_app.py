from app import app

def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Jenkins" in resp.data
