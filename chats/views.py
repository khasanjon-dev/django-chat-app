from django.shortcuts import render

from users.models import User


def index(request):
    users = User.objects.all()
    detail = {
        'users': users
    }
    return render(request, 'index.html', detail)


def chat(request):
    return render(request, 'chats/chat.html')
