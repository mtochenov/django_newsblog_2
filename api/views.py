from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from news.models import News, Category

from rest_framework import generics, viewsets

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import NewsSerializer


class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly, )  # this class include IsAdminUser class


class NewsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class NewsListAPIView(generics.ListAPIView):  # Обычное представление для API
#     queryset = News.objects.all()             # без указания прав доступа
#     serializer_class = NewsSerializer
#
#
# class NewsViewSet(viewsets.ModelViewSet):  # Представление для API
#     queryset = News.objects.all()          # с подключением routers в url
#     serializer_class = NewsSerializer      # для автоматической подстановки адреса в url