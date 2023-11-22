from django.db.models import Model, ForeignKey, CASCADE, CharField, BooleanField, DateTimeField

from users.models import User


class Chat(Model):
    sender = ForeignKey(User, CASCADE, 'sender')
    receiver = ForeignKey(User, CASCADE, 'receiver')
    message = CharField(max_length=1000)

    is_read = BooleanField(default=False)
    is_edited = BooleanField(default=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
