from django.contrib.auth.models import User, AnonymousUser
from django.db.models import Model, ForeignKey, SET, TextField, DateTimeField


class Message(Model):
    sender_user = ForeignKey(User, SET(AnonymousUser.id), 'sender')
    receiver_user = ForeignKey(User, SET(AnonymousUser.id), 'receiver')
    message = TextField()
    timestamp = DateTimeField(auto_now_add=True)
