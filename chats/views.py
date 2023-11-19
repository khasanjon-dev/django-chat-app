from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string
from django.views import View

from chats.models import Room, Message


class GetAllUsers(LoginRequiredMixin, View):
    def get(self, request):
        """
        to get the list of all users from the database
        """
        users = User.objects.all()
        detail = {
            'users': users
        }
        return render(request, 'all-users.html', detail)

    def post(self, request):
        """
        to get the sender and receiver users and connect them with their respective room
        """
        sender_id = request.user.id
        receiver_id = request.POST['users']
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        # setting the receiver as a session variable
        request.session['receiver'] = receiver

        # check if the sender and receiver already have a room
        room = Room.objects.filter(Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender))

        # fetches the room name if a room already exists
        if room:
            room_name = room[0].name

        # create a new room
        else:
            new_room = get_random_string(10)
            while True:
                room_exists = Room.objects.filter(name=new_room)
                if room_exists:
                    new_room = get_random_string(10)
                else:
                    break
            create_room = Room.objects.create(sender=sender, receiver=receiver, name=new_room)
            create_room.save()
            room_name = create_room.name
        return redirect('room', room_name=room_name)


class ChatRoom(LoginRequiredMixin, View):
    queryset = Room.objects.all()

    def get(self, request, room_name, *args, **kwargs):
        room = get_object_or_404(Room, name=self.kwargs.get('room_name'))
        sender_id = request.user.id
        sender_username = User.objects.get(id=sender_id).username

        # sets up the user as sender user for chating
        if room.receiver_id == sender_id:
            receiver_id = room.sender_id
        else:
            receiver_id = room.receiver_id

        # get all the previous messages from the database
        messages = Message.objects.filter(
            Q(sender_id=sender_id, receiver_id=receiver_id) | Q(sender_id=receiver_id, receiver_id=sender_id)).order_by(
            'timestamp')
        detail = {
            'name': room_name,
            'sender_id': sender_id,
            'receiver_id': receiver_id,
            'messages': messages,
            'sender_username': sender_username
        }
        return render(request, 'room.html', detail)
