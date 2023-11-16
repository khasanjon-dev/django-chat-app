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
        print(request.user)
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'chats/all-users.html', context)

    def post(self, request):
        """
        to get the sender and receiver users and connect them with their respective room
        """
        sender_id = request.user.id
        receiver = request.POST['users']
        sender_user = User.objects.get(id=sender_id)
        receiver_user = User.objects.get(id=receiver)
        # setting the receiver as a session variable
        request.session['receiver_user'] = receiver

        # check if the sender and receiver already have a room
        get_room = Room.objects.filter(
            Q(sender_user=sender_user, receiver_user=receiver_user) | Q(sender_user=receiver_user,
                                                                        receiver_user=sender_user))
        if get_room:
            room_name = get_room[0].room_name

        # creates a new room if room doesn't exist
        else:
            new_room = get_random_string(10)
            while True:
                room_exists = Room.objects.filter(room_name=new_room)
                if room_exists:
                    new_room = get_random_string(10)
                else:
                    break
            create_room = Room.objects.create(
                sender_user=sender_user,
                receiver_user=receiver_user,
                room_name=new_room
            )
            create_room.save()
            room_name = create_room.room_name
        return redirect('room', room_name=room_name)


class ChatRoom(LoginRequiredMixin, View):
    queryset = Room.objects.all()

    def get(self, request, room_name, *args, **kwargs):
        room = get_object_or_404(Room, room_name=self.kwargs.get('room_name'))
        sender = request.user.id
        sender_name = User.objects.get(id=sender).username

        if room.receiver_user.id == sender_name:
            receiver = room.sender_user.id
        else:
            receiver = room.receiver_user.id
        message = Message.objects.filter(
            Q(sender_user=sender, receiver_user=receiver) | Q(sender_user=receiver, receiver_user=sender)).order_by(
            'timestamp')
        context = {
            'room_name': room_name,
            'sender_id': sender,
            'receiver_id': receiver,
            'message': message,
            'sender_name': sender_name
        }
        return render(request, 'chats/room.html', context)
