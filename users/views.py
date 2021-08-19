from django.shortcuts import render
from users.forms import CustomUserCreationForm


def login(request):
    return render(request, 'login.html')


def sign_in(request):
    if request.method == 'POST':
        new_user = CustomUserCreationForm(request.POST)
        if new_user.is_valid():
            print('Usuário válido!!!')
        else:
            print(new_user)
    return render(request, 'sign_in.html')
