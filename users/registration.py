from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login


def register(username, password):
    User.objects.create_user(username=username, password=password)


def login_user(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return True
    return False
