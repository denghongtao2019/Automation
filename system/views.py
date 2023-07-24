from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from system.models import Model


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            error_msg = '用户名或密码错误'
    else:
        error_msg = ''

    return render(request, 'login.html', {'error_msg': error_msg})


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def report(request):
    data = Model().get_json_data()
    return render(request, 'report.html', {'data': data})

