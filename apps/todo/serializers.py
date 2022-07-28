from rest_framework import serializers
from .models import *
from ..team_user.models import Account


class TodoSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Todo
        fields = ('id', 'author', 'title',  'description', 'is_finished', 'status', 'priority', 'deadline', 'created_at')
        extra_kwargs = {
            'author': {'required': False}
        }
