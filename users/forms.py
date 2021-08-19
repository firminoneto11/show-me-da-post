from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = 'first_name', 'last_name', 'email', 'password1', 'password2'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.email = self.cleaned_data.get('username')  # Only line that is overwritten
        if commit:
            user.save()
        return user
