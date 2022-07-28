from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .serializers import TaskSerializer, TaskCreateUpdateSerializer, SendTaskSerializer, CommentSerializer, \
    SendTaskCreateSerializer
from rest_framework import generics, status, response, viewsets, mixins
from .models import Task, SendTask, Comment
from rest_framework.permissions import IsAuthenticated
from ..team_user.permissions import IsAdminUserForAccount


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Task.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title_icontains=query) |
                Q(description_icontains=query) |
                Q(status=query) |
                Q(priority=query)
            )
        return queryset_list


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateUpdateSerializer
    permission_classes = (IsAdminUserForAccount,)


class TaskMixin(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateUpdateSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class TaskUpdateAPIView(TaskMixin):
    queryset = Task.objects.all()
    serializer_class = TaskCreateUpdateSerializer
    permission_classes = (IsAdminUserForAccount,)
    lookup_field = 'pk'


class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateUpdateSerializer
    permission_classes = (IsAdminUserForAccount,)
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_deleted = True


class SendTaskListAPIView(generics.ListAPIView):
    queryset = SendTask.objects.all()
    serializer_class = SendTaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset().filter(sender_id=self.request.user.id)
        return qs


class SendTaskCreateAPIView(generics.CreateAPIView):
    queryset = SendTask.objects.all()
    serializer_class = SendTaskCreateSerializer
    permission_classes = (IsAdminUserForAccount,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(sender=user)


# class CommentListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentCreateSerializer
#     permission_classes = (IsAuthenticated,)
#


class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    search_fields = ['name']
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name_icontains=query)
            )
        return queryset_list


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
