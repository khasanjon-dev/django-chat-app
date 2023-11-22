from django.core.exceptions import ValidationError
from django.forms import Form
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
