from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from users.models import User


@login_required(login_url='login')
def index_view(request):
    users = User.objects.order_by('-date_joined')
    context = {
        'users': users
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def chat_view(request, pk):
    date = datetime.now()
    user = User.objects.get(id=pk)
    users = User.objects.all()
    context = {
        'users': users,
        'user': user,
        'date': date
    }
    return render(request, 'chats/chat.html', context)
