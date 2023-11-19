from django.contrib.auth.models import User, AnonymousUser
from django.db.models import Model, ForeignKey, SET, TextField, DateTimeField, CharField


class Message(Model):
    message = TextField()
    timestamp = DateTimeField(auto_now_add=True)
    # relationships
    sender = ForeignKey(User, SET(AnonymousUser.id), 'senders')
    receiver = ForeignKey(User, SET(AnonymousUser.id), 'receivers')


class Room(Model):
    name = CharField(max_length=250, unique=True)
    # relationships
    sender = ForeignKey(User, SET(AnonymousUser.id), 'room_senders')
    receiver = ForeignKey(User, SET(AnonymousUser.id), 'room_receivers')

    def __str__(self):
        return self.name
