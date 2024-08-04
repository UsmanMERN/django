from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BookType(models.Model):
    BOOKS_TYPE_CHOICES = [
        ("FC", "Fiction"),
        ("NFC", "Non-Fiction"),
        ("SC", "Science Fiction"),
        ("BI", "Biography"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="learnings/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=BOOKS_TYPE_CHOICES)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


# one to many


class BookReview(models.Model):
    book = models.ForeignKey(BookType, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    commet = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.book.name}"


# many to many


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    book_types = models.ManyToManyField(BookType, related_name="stores")

    def __str__(self):
        return self.name


# one to one


class BookCertificate(models.Model):
    book = models.OneToOneField(
        BookType, on_delete=models.CASCADE, related_name="certificate"
    )
    certificate_numer = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.book.name}"
