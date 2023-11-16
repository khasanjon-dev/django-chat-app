from django.contrib.auth.models import User, AnonymousUser
from django.db.models import Model, ForeignKey, SET, TextField, DateTimeField, CharField


class Message(Model):
    sender_user = ForeignKey(User, SET(AnonymousUser.id), 'sender')
    receiver_user = ForeignKey(User, SET(AnonymousUser.id), 'receiver')
    message = TextField()
    timestamp = DateTimeField(auto_now_add=True)


class Room(Model):
    sender_user = ForeignKey(User, SET(AnonymousUser.id), 'room_sender')
    receiver_user = ForeignKey(User, SET(AnonymousUser.id), 'room_receiver')
    room_name = CharField(max_length=200, unique=True)

    def __str__(self):
        return self.room_name
