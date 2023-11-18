from django.urls import path

from chats.views import index

urlpatterns = [
    path('', index, name='index')
]
