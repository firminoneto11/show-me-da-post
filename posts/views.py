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
        post_data = {key: request.POST.get(key) for key in request.POST.keys()}
        post_form = PostCreationForm(post_data)
        if post_form.is_valid():
            # TODO: Save in the database and inform the user through some notification that it's post was a success
            if int(post_data.get("author_id")) == request.user.pk:
                del post_data["csrfmiddlewaretoken"]
                post_data = {key: post_form.cleaned_data.get(key) for key in post_data.keys()}
                Post(**post_data).save()
                request.method = "GET"
                context.update({"success": True})
                return render(request, 'index.html', context)
            else:
                # TODO: Do something if the user changed the user's ID
                pass
        else:
            # TODO: Do something to inform the user that he typed something weird
            return render(request, 'index.html', context)
    return render(request, 'index.html', context)


def log_out(request):
    logout(request)
    return redirect(to='login')
