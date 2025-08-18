from django.urls import path
from .views import AuthorListCreateView, BookListCreateView, MemberListCreateView, BorrowRecordListCreateView

urlpatterns = [
    path("authors/", AuthorListCreateView.as_view(), name="authors"),
    path("books/", BookListCreateView.as_view(), name="books"),
    path("members/", MemberListCreateView.as_view(), name="members"),
    path("borrow-records/", BorrowRecordListCreateView.as_view(), name="borrow-records"),
]
