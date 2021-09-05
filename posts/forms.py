from django import forms
from posts.models import Posts


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = 'author', 'title', 'post_content'

    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        "placeholder": "Your title goes here"
    }))

    post_content = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        "placeholder": "Type your post here",
        "rows": 3
    }))


"""
1- The biggest issue when trying to render the "author" field, is that the name i used on the form was "author_id" while 
the name of the actual field was only "author". That's why the errors kept coming over;

2 - After the insight i just had to correct everybody that had "author_id" was a name and rename it to "author". Also, 
when doing the verification in the view to check if the request.user is the same from the input field "author", we just
need to compare if they are the same object instance of the current User model by doing something like:

if post_form.cleaned_data.get("author").pk == request.user.pk:

With this, we can confirm if the user instance of cleaned data is the same of the current user that is logged in. After
this, just go ahead and save the form normally into the database;
"""
