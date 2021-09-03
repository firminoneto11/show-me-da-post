from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from posts.forms import PostCreationForm
from posts.models import Post


@login_required(login_url='login')
def home(request):
    context = {"form": PostCreationForm(), "posts": Post.objects.raw(
        """
        SELECT p.id, u.first_name, u.last_name, p.title, p.post_content, p.posted_on
        FROM USERS_CUSTOMUSER AS "u" INNER JOIN POSTS_POST AS "p" ON p.author_id = u.id
        ORDER BY p.posted_on DESC;
        """
    )}
    if request.method == "POST":
        post_form = PostCreationForm(request.POST)
        if post_form.is_valid():
            if post_form.cleaned_data.get("author").pk == request.user.pk:
                post_form.save(commit=True)
                context.update({"success": "Posted successfully!"})
                return render(request, 'index.html', context)
            else:
                context.update({"error": "An error occurred. Please, try again..."})
        else:
            context.update({"error": "An error occurred. Please, try again..."})
    return render(request, 'index.html', context)


@login_required(login_url='login')
def remove(request):
    context = {'posts': Post.objects.raw(
        """
        SELECT p.id, u.first_name, u.last_name, p.title, p.post_content, p.posted_on
        FROM USERS_CUSTOMUSER AS "u" INNER JOIN POSTS_POST AS "p" ON p.author_id = u.id
        WHERE p.author_id = %s
        ORDER BY p.posted_on DESC;
        """ % request.user.pk
    )}
    if request.method == 'POST':
        post = Post.objects.get(pk=request.POST.get("post_id"))
        post.delete()
        context.update({"success": "Post removed successfully!"})
    return render(request, 'remove.html', context)


def log_out(request):
    logout(request)
    return redirect(to='login')
