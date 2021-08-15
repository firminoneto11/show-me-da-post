from django.shortcuts import render, redirect
from users.views import login


def home(request):
    if request.user.is_anonymous:
        return redirect(login)        
    else:
        return render(request, 'index.html')
