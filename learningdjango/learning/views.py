from django.http import HttpResponse
from django.shortcuts import render
from .models import BookType
from django.shortcuts import get_object_or_404


def all_learners(request):
    books = BookType.objects.all()

    return render(request, "learning/learning.html", {"books": books})


def book_details(request, book_id):
    book = get_object_or_404(BookType, pk=book_id)
    return render(request, "learning/details.html", {"book": book})
