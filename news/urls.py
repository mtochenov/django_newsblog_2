from django.urls import path, re_path, include
from .views import *

# router = routers.SimpleRouter()
# router.register('', NewsViewSet)

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('add_news/', add_news, name='add_news'),

    # path('api/', NewsListAPIView.as_view()),  # Поменяли данный класс представлений на другой
    # path('api/', include(router.urls)),  # Используем вместе с router

    path('api/', NewsAPIList.as_view()),
    path('api/<int:pk>/', NewsAPIUpdate.as_view()),
    path('api/delete/<int:pk>/', NewsAPIDestroy.as_view()),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
