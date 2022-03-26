from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login,logout


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Успешная регистрация')
            return redirect('news_list')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/registration.html', {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news_list')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/user_login.html', {'form': form})


def user_logout_view(request):
    logout(request)
    return redirect('user_login')
