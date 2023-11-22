from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm
from django.shortcuts import get_object_or_404

from users.models import User


class LoginForm(Form):
    def clean_password(self):
        username = self.data.get('username')
        password = self.data.get('password')
        user = get_object_or_404(User, username=username)
        if user.check_password(password):
            context = 'Password or Username do not match'
            raise ValidationError(context)
        return password


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and self._meta.objects.filter(email__iexact=email).exists():
            self._update_errors(
                ValidationError(
                    {
                        'email': self.instance.unique_error_message(
                            self._meta.model, ['email']
                        )
                    }
                )
            )
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and self._meta.objects.filter(username__ixact=username).exists():
            self._update_errors(
                ValidationError(
                    {
                        'username': self.instance.unique_error_message(
                            self._meta.model, ['username']
                        )
                    }
                )
            )
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            message = 'Password do not match'
            raise ValidationError(message)
        return make_password(password)
