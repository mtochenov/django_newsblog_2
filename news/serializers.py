from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = ('title', 'content', 'category', 'user', )
