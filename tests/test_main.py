import pytest
from fastapi.testclient import TestClient

from crisco import main

client = TestClient(main.app)


@pytest.mark.asyncio
async def test_load_config():
    assert await main.load_config() == {
        "urls": {"root": "https://shoup.io", "foo": "https://baz"}
    }


def test_read_path():
    response = client.get("/foo", allow_redirects=False)
    assert response.status_code == 307
    assert "location" in response.headers
    assert response.headers["location"] == "https://baz"


def test_read_root():
    response = client.get("/", allow_redirects=False)
    assert response.status_code == 307
    assert "location" in response.headers
    assert response.headers["location"] == "https://shoup.io"

def test_404():
    response = client.get("/doesnotexist")
    assert response.status_code == 404

def test_health_check():
    response = client.get("/-/health")
    assert response.status_code == 200
    assert response.text == "OK"
