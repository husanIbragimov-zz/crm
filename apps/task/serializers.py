from rest_framework import serializers
from .models import Task, SendTask, Comment
from ..team_user.models import Account
from ..team_user.serializers import AccountSerializer


class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField(read_only=True)
    priority_display = serializers.SerializerMethodField(read_only=True)

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_priority_display(self, obj):
        return obj.get_priority_display()

    class Meta:
        model = Task
        fields = (
            'id', 'title', 'description', 'priority', 'priority_display', 'status', 'status_display', 'supervisor',
            'superuser', 'group', 'is_deleted', 'updated_at', 'created_at')


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'title', 'description', 'priority', 'status', 'superuser', 'group', 'deadline')


class SendTaskCreateSerializer(serializers.ModelSerializer):
    # sender = serializers.CharField(source='sender.first_name', read_only=True)
    # receiver = serializers.CharField(source='receiver.first_name')
    # group = serializers.CharField(source='group.name', read_only=True)

    class Meta:
        model = SendTask
        fields = ('id', 'task', 'receiver', 'message', 'group')
        # extra_kwargs = {
        #     'task': {'read_only': True},
        # }


class SendTaskSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.first_name', read_only=True)
    receiver = serializers.CharField(source='receiver.first_name', read_only=True)
    group = serializers.CharField(source='group.name', read_only=True)

    class Meta:
        model = SendTask
        fields = ('id', 'task', 'sender', 'receiver', 'message', 'group')


class CommentSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField(source='task.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'task_id', 'title', 'description']
