

# Create your models here.
from djongo import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class BorrowRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.member} borrowed {self.book}"
