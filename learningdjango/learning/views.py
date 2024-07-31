from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def all_learners(request):
    return render(request, "learning/learning.html")
