from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from users.models import User


def index(request):
    users = User.objects.order_by('-date_joined')
    context = {
        'users': users
    }
    return render(request, 'index.html', context)


@login_required
def chat(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'chats/chat.html', context)
