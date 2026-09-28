import pytest

from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'


def test_count(client):
    response = client.get('/count')
    assert response.status_code == 200
    assert response.data == b'Count page!'


def test_something_else(client):
    response = client.get('/somethingelse')
    assert response.status_code == 200
    assert response.data == b'Something else page!'
