from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from news.models import News

from rest_framework import generics

from .permissions import IsOwnerOrReadOnly
from .serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    """use all requests"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

    def perform_update(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


# class NewsAPIList(generics.ListCreateAPIView):
#     """GET, POST requests"""
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )


# class NewsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     """GET, PUT, PATCH, DELETE requests"""
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     permission_classes = (IsOwnerOrReadOnly, )
#
#     def get_queryset(self):
#         return News.objects.filter(user=self.request.user)
