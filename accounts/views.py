from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/registration.html', {'form': form})


def authorization_view(request):
    return render(request, 'accounts/authorization.html')

