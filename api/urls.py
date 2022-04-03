from django.urls import path, re_path, include
from .views import *


# router = routers.SimpleRouter()
# router.register('', NewsViewSet)

urlpatterns = [
    path('', NewsAPIList.as_view()),
    path('<int:pk>/', NewsAPIDetail.as_view()),

    path('api-auth/', include('rest_framework.urls')),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # path('', include(router.urls)),  # Используем вместе с router
]
