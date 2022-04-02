from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('add_news/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]
