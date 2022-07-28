from rest_framework import serializers
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.id')

    class Meta:
        model = Chat
        fields = ('id', 'sender', 'receiver', 'message', 'is_read',)
        extra_kwargs = {
            'sender': {'required': False}
        }
