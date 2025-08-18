import pytest
from rest_framework.test import APIClient
from library.models import BorrowRecord, Member, Book, Author

@pytest.mark.django_db
def test_create_borrow_record():
    author = Author.objects.create(name="Mark Twain", bio="Author")
    book = Book.objects.create(title="Tom Sawyer", author=author, isbn="9876543210123", available=True)
    member = Member.objects.create(name="Charlie", email="charlie@example.com")

    client = APIClient()
    response = client.post("/borrow-records/", {
        "member": member.id,
        "book": book.id
    }, format="json")

    assert response.status_code == 201
    assert BorrowRecord.objects.count() == 1
    assert BorrowRecord.objects.first().book.title == "Tom Sawyer"
