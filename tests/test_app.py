import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_app(client):
    # Test the root URL
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, DevOps World!' in response.data

    # Test a non-existent URL
    response = client.get('/nonexistent')
    assert response.status_code == 404