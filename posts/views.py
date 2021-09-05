from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from posts.forms import PostCreationForm
from posts.models import Posts


@login_required(login_url='login')
def home(request):
    context = {"form": PostCreationForm(), "posts": Posts.objects.raw(
        """
        SELECT p.id, u.first_name, u.last_name, p.title, p.post_content, p.posted_on
        FROM USERS AS "u" INNER JOIN POSTS AS "p" ON p.author_id = u.id
        ORDER BY p.posted_on DESC;
        """
    )}
    if request.method == "POST":
        post_form = PostCreationForm(request.POST)
        if post_form.is_valid():
            if post_form.cleaned_data.get("author").pk == request.user.pk:
                try:
                    post_form.save(commit=True)
                except Exception:
                    # If some error occur while trying to INSERT the data into the database
                    context.update({"error": "An error occurred. Please, try again..."})
                else:
                    context.update({"success": "Posted successfully!"})
            else:
                # If the user changed the "author_id" in the html page
                context.update({"error": "Sorry, we couldn't post that..."})
        else:
            # If the form is not valid, containing some sql injection for example
            context.update({"error": "An error occurred. Please, try again..."})
    return render(request, 'index.html', context)


@login_required(login_url='login')
def update(request):
    context = {"form": PostCreationForm(), "posts": Posts.objects.raw(
        """
        SELECT p.id, u.first_name, u.last_name, p.title, p.post_content, p.posted_on
        FROM USERS AS "u" INNER JOIN POSTS AS "p" ON p.author_id = u.id
        WHERE p.author_id = %s
        ORDER BY p.posted_on DESC;
        """ % request.user.pk
    )}
    if request.method == "POST":
        update_post_form = PostCreationForm(request.POST)
        if update_post_form.is_valid():
            try:
                # Getting the current post ID in order to do a verification if the user didn't change the post_id value
                post_id = int(request.POST.get("post_id"))
            except Exception:
                context.update({"error": "Post ID invalid"})
            else:
                # Checking if the post id exists within the posts posted by the current user
                post_exists = Posts.objects.all().filter(author_id=request.user.pk).filter(id=post_id).exists()

                # Verifying the given data
                if (update_post_form.cleaned_data.get("author").pk != request.user.pk) or (not post_exists):
                    # If the user changed the "author_id" or the "post_id" in the html page
                    context.update({"error": "Sorry, we couldn't post that..."})
                else:
                    post_instance = Posts.objects.get(pk=post_id)
                    update_post_form = PostCreationForm(request.POST, instance=post_instance)
                    try:
                        update_post_form.save(commit=True)
                    except Exception:
                        # If some error occur while trying to UPDATE the data into the database
                        context.update({"error": "An error occurred. Please, try again..."})
                    else:
                        context.update({"success": "Post updated successfully!"})
        else:
            # If the form is not valid, containing some sql injection for example
            context.update({"error": "An error occurred. Please, try again..."})
    return render(request, 'update.html', context)


@login_required(login_url='login')
def remove(request):
    context = {'posts': Posts.objects.raw(
        """
        SELECT p.id, u.first_name, u.last_name, p.title, p.post_content, p.posted_on
        FROM USERS AS "u" INNER JOIN POSTS AS "p" ON p.author_id = u.id
        WHERE p.author_id = %s
        ORDER BY p.posted_on DESC;
        """ % request.user.pk
    )}
    if request.method == 'POST':
        try:
            post = Posts.objects.get(pk=request.POST.get("post_id"))
            post.delete()
        except Exception:
            # If some error occur while trying to DELETE the data in the database
            context.update({"error": "An error occurred..."})
        else:
            context.update({"success": "Post removed successfully!"})
    return render(request, 'remove.html', context)


def log_out(request):
    logout(request)
    return redirect(to='login')


# Quick tip
# Posts.objects.all().filter(author_id=request.user.pk).values("id") -> A approach for getting only the
# ID fields with a WHERE clause. Equivalent to the following sql query:
# SELECT ID FROM POSTS WHERE AUTHOR_ID = %s
