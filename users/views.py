from django.shortcuts import redirect, render
from users.forms import CustomUserCreationForm, LoginForm


def login(request):
    context = {'form': LoginForm()}
    if 'success' in request.session.keys():
        context.update({'success': request.session.get('success')})  # Saving the data that came from the session storage
        del request.session['success']  # Deleting the data from the session storage
        return render(request, 'login.html', context)
    return render(request, 'login.html', context)


def sign_in(request):
    if request.method == 'POST':
        new_user = CustomUserCreationForm(request.POST)
        if new_user.is_valid():
            request.session.update({'success': 'User created successfully!'})
            new_user.save(commit=True)
            return redirect('login')
        else:
            context = {'form': new_user, 'errors': new_user.errors}
            return render(request, 'sign_in.html', context)
    context = {'form': CustomUserCreationForm()}
    return render(request, 'sign_in.html', context)
