from django.urls import re_path

from chats.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/public_room/', ChatConsumer.as_asgi())
]
