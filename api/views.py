from rest_framework.viewsets import ModelViewSet

from news.models import News
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
