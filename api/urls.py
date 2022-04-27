from django.urls import path, re_path, include
from rest_framework import routers

from .views import *


router = routers.SimpleRouter()
router.register(r'', NewsViewSet)

urlpatterns = [
    # path('', NewsAPIList.as_view()),
    # path('<int:pk>/', NewsAPIDetail.as_view()),
    path('', include(router.urls)),  # Используем вместе с router

    path('api-auth/', include('rest_framework.urls')),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
