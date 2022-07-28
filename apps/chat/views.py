from .serializers import ChatSerializer
from rest_framework import generics, permissions
from .models import Chat


class ChatListCreateAPIView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        super().get_queryset().filter(sender_id=self.request.user.id)


