import pytest
from rest_framework.test import APIClient
from library.models import Book, Author

@pytest.mark.django_db
def test_create_book():
    author = Author.objects.create(name="J.R.R. Tolkien", bio="LOTR author")
    client = APIClient()
    response = client.post("/books/", {
        "title": "The Hobbit",
        "author": author.id,
        "isbn": "1234567890123",
        "available": True
    }, format="json")

    assert response.status_code == 201
    assert Book.objects.count() == 1
    assert Book.objects.first().title == "The Hobbit"
