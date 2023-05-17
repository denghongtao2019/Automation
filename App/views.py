from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    # return HttpResponse("Hello Word!")
    return render(request, "index.html")


def user(request):
    return render(request, "user.html")


def login(request):
    return render(request, "login.html")
