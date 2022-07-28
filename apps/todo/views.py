from django.db.models import Q, Count
from django.db.models.functions import TruncDay
from rest_framework import generics, permissions, mixins, viewsets, routers
from rest_framework.response import Response

from .models import *
from .serializers import *
from ..team_user.permissions import *


class TodoCreateAPIView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrReadOnlyForAccount,)


class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrReadOnlyForAccount,)

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('query')
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        month = self.request.GET.get('month')
        if query:
            qs = qs.filter(
                Q(title_icontains=query) |
                Q(description_icontains=query)
            )
        if status:
            qs = qs.filter(status=status)
        if priority:
            qs = qs.filter(priority=priority)
        if month:
            qs = qs.filter(created_at__month=month)

        return qs


class TodoMixin(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class TodoRDAPIView(generics.RetrieveDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


class TodoAPIView(TodoMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)


# class TodoViewSets(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# routers = routers.DefaultRouter()
# routers.register('router/', TodoViewSets)

