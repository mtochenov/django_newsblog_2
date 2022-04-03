from rest_framework.permissions import IsAuthenticatedOrReadOnly

from news.models import News

from rest_framework import generics

from .permissions import IsOwnerOrReadOnly
from .serializers import NewsSerializer


class NewsAPIList(generics.ListCreateAPIView):
    """GET, POST requests"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class NewsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    """GET, PUT, PATCH, DELETE requests"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly, )
