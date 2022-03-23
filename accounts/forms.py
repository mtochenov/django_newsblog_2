from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Укажите оригинальное имя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ведите пароль'}))
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ведите ваш email'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ведите пароль'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
