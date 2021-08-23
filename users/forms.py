from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(max_length=128)

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = 'first_name', 'last_name', 'email', 'password1', 'password2'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.username = self.cleaned_data.get('email')  # Only line that is overwritten
        if commit:
            user.save()
        return user
