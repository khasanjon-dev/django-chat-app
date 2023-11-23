from django.urls import path

from chats.views import chat_view, index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('chat/<int:pk>', chat_view, name='chat')
]
