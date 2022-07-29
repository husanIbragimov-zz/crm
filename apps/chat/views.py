from django.db.models import Q
from rest_framework.response import Response

from .serializers import ChatSerializer
from rest_framework import generics, permissions, status
from .models import Chat


class ChatCreateAPIView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        sender = self.request.user
        serializer.save(sender=sender)


class ChatListAPIView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset().filter(is_read=False).order_by('-id')
        qs = qs.filter(Q(sender_id=self.request.user.id) | Q(receiver_id=self.request.user.id))
        return qs

