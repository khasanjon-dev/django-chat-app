from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models import CharField, DateTimeField, EmailField, ImageField


class User(AbstractUser):
    first_name = CharField(max_length=150, null=True, blank=True)
    last_name = CharField(max_length=150, null=True, blank=True)
    email = EmailField(unique=True)
    date_joined = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True, null=True)
    # file
    image = ImageField(upload_to='users/images', default='users/images/default.jpg')

    def __str__(self):
        return self.email + ' ' + self.username
