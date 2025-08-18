import pytest
from rest_framework.test import APIClient
from library.models import Member

@pytest.mark.django_db
def test_create_member():
    client = APIClient()
    response = client.post("/members/", {"name": "Alice", "email": "alice@example.com"}, format="json")
    assert response.status_code == 201
    assert Member.objects.count() == 1

@pytest.mark.django_db
def test_get_members():
    Member.objects.create(name="Bob", email="bob@example.com")
    client = APIClient()
    response = client.get("/members/")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Bob"
