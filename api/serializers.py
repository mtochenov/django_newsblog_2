from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'category', 'user')
