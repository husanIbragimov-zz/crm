from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Notification
        fields = ('id', 'user', 'notification', 'is_read', 'created_at')


class NotificationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'notification',)
