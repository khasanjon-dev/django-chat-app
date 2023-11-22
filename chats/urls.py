from django.urls import path

from chats.views import index_view, chat_view

urlpatterns = [
    path('', index_view, name='index'),
    path('chat/', chat_view, name='chat')
]
