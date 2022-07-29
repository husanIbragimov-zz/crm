from rest_framework import status, generics, permissions, response, views
from .serializers import NotificationSerializer, NotificationCreateSerializer
from ..team_user.permissions import IsAdminUserForAccount
from .models import Notification
from drf_yasg import openapi


class NotificationListAPIView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset().filter(is_read=False)
        return qs


class NotificationCreateAPIView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationCreateSerializer
    permission_classes = (IsAdminUserForAccount,)

