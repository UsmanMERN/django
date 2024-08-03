from django.db import models
from django.utils import timezone


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
