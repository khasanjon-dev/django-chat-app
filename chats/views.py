from django.shortcuts import render

from chats.models import Room


def index_view(request):
    detail = {
        'rooms': Room.objects.all()
    }
    return render(request, 'index.html', detail)


def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    detail = {
        'room': chat_room
    }
    return render(request, 'room.html', detail)


