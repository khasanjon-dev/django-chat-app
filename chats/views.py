from django.shortcuts import render

from chats.models import Room


def index_view(request):
    detail = {
        'rooms': Room.objects.all()
    }
    return render(request, 'index.html', detail)



