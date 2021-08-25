from django.shortcuts import redirect, render
from users.forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login


def log_in(request):
    context = {'form': LoginForm()}
    if 'success' in request.session.keys():
        context.update({'success': request.session.get('success')})  # Saving the data that came from the session
        # storage
        del request.session['success']  # Deleting the data from the session storage
    if request.method == 'POST':
        user_data = LoginForm(request.POST)
        if user_data.is_valid():
            user_data = (user_data.cleaned_data.get('email'), user_data.cleaned_data.get('password'))
            user = authenticate(request, username=user_data[0], password=user_data[1])
            if user is not None:
                login(request, user)
                return redirect(to='home')
            else:
                # Email or password incorrect
                context.update({'error': 'Email or password incorrect'})
        else:
            # Invalid information
            context.update({'error': 'Invalid information'})
    return render(request, 'login.html', context)


def sign_in(request):
    if request.method == 'POST':
        new_user = CustomUserCreationForm(request.POST)
        if new_user.is_valid():
            request.session.update({'success': 'User created successfully!'})
            new_user.save(commit=True)
            return redirect(to='login')
        else:
            context = {'form': new_user, 'errors': new_user.errors}
            return render(request, 'sign_in.html', context)
    context = {'form': CustomUserCreationForm()}
    return render(request, 'sign_in.html', context)
