from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def chat(request):
    return render(request, 'chats/chat.html')
