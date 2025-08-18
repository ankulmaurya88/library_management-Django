from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Author, Book, Member, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, MemberSerializer, BorrowRecordSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowRecordListCreateView(generics.ListCreateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
