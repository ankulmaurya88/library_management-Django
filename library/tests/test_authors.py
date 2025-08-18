import pytest
from rest_framework.test import APIClient
from library.models import Author

@pytest.mark.django_db
def test_create_author():
    client = APIClient()
    response = client.post("/authors/", {"name": "J.K. Rowling", "bio": "Author of Harry Potter"}, format="json")
    assert response.status_code == 201
    assert Author.objects.count() == 1

@pytest.mark.django_db
def test_get_authors():
    Author.objects.create(name="George Orwell", bio="1984 and Animal Farm")
    client = APIClient()
    response = client.get("/authors/")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "George Orwell"
