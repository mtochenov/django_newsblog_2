from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),
    path('authorization/', views.authorization_view, name='authorization'),
    # path('logout/', views.logout_view, name='logout'),
]
