import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

from chats.models import Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # save message in the database
    def save_message(self, message, sender, receiver):
        sender = User.objects.get(id=sender)
        receiver = User.objects.get(id=receiver)
        data = {
            'message': message,
            'sender': sender,
            'receiver': receiver
        }
        new_message = Message.objects.create(**data)
        new_message.save()

    # receive message frome WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        receiver = text_data_json['receiver']
        sender_username = text_data_json['sender_name']
        self.save_message(message, sender, receiver)

        # send message to room group
        data = {
            'type': 'chat_message',
            'message': message,
            'sender': sender,
            'receiver': receiver,
            'sender_name': sender_username
        }
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            data
        )
