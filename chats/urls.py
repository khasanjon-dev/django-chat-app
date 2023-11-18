from django.urls import path

from chats.views import index_view, room_view

urlpatterns = [
    path('', index_view, name='chat-index'),
    path('<str:room_name>/', room_view, name='chat-room'),
]
