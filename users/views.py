from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def sign_in(request):
    return render(request, 'sign_in.html')
