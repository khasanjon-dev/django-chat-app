from django.shortcuts import render

from users.models import User


def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'index.html', context)


def chat(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'chats/chat.html', context)
