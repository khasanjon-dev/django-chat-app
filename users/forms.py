from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm

from users.models import User


class LoginForm(Form):
    def clean_password(self):
        password = self.data.get('password')
        password = make_password(password)
        return password


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            message = 'Email already used'
            raise ValidationError(message)
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            message = 'Username already used'
            raise ValidationError(message)
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            message = 'Password do not match'
            raise ValidationError(message)
        return make_password(password)
