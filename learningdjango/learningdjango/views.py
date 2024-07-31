from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, Mars. Am learning Django and this is home page")
    return render(request, "website/index.html")


def about(request):
    return HttpResponse("Hello, Mars. Am learning Django and this is About page")


def contact(request):
    return HttpResponse("Hello, Mars. Am learning Django and this is contact page")
