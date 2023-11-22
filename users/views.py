from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from users.forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                message = 'email or password wrong'
                messages.add_message(request, messages.ERROR, message)
                return render(request, 'users/login.html')
            return redirect('index')
    return render(request, 'users/login.html')


def register_view(request):
    return render(request, 'users/register.html')
