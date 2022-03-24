from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),
    path('user_login/', views.user_login_view, name='user_login'),
    # path('logout/', views.logout_view, name='logout'),
]
