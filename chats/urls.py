from django.urls import path

from chats.views import GetAllUsers, ChatRoom

urlpatterns = [
    path('rooms/', GetAllUsers.as_view(), name='rooms'),
    path('rooms/<str:room_name>/', ChatRoom.as_view(), name='room')
]
