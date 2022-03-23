from django.urls import path, re_path, include
from .views import *


urlpatterns = [
    path('', NewsAPIList.as_view()),
    path('<int:pk>/', NewsAPIUpdate.as_view()),
    path('delete/<int:pk>/', NewsAPIDestroy.as_view()),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
