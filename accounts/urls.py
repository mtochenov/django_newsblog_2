from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),
    path('user_login/', views.user_login_view, name='user_login'),
    path('user_logout/', views.user_logout_view, name='user_logout'),
]
