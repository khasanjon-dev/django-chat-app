from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from shared.decorators import anonymous_required
from users.forms import LoginForm, RegisterForm


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            context['error'] = 'username or password do not match!'
    return render(request, 'users/login.html', context)


@anonymous_required('/')
def register_view(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['errors'] = form.errors

    return render(request, 'users/register.html', context)
