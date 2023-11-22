from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db.models import (CharField, DateTimeField, EmailField)


class User(AbstractUser):
    first_name = CharField(max_length=150, null=True, blank=True)
    last_name = CharField(max_length=150, null=True, blank=True)
    email = EmailField(unique=True)

    updated_at = DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.email + ' ' + self.username
