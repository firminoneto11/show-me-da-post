from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from posts.forms import PostCreationForm


@login_required(login_url='login')
def home(request):
    context = {'form': PostCreationForm()}
    if request.method == "POST":
        post_form = PostCreationForm(request.POST)
        if post_form.is_valid():
            # Save in the database and inform the user through some notification that it's post has a success
            pass
        else:
            # Do something to inform the user that he typed something weird
            pass
        return render(request, 'index.html', context)
    return render(request, 'index.html', context)


def log_out(request):
    logout(request)
    return redirect(to='login')
