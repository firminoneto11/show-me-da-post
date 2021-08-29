from django import forms
from posts.models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'author_id', 'title', 'post_content'

    author_id = forms.IntegerField()

    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        "placeholder": "Your title goes here"
    }))

    post_content = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        "placeholder": "Type your post here"
    }))
