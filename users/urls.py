from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
