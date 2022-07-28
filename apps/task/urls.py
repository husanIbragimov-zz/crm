from django.urls import path
from . import views

urlpatterns = [
    # task
    path('list/', views.TaskListAPIView.as_view()),
    path('create/', views.TaskCreateAPIView.as_view()),
    path('update/<int:pk>/', views.TaskUpdateAPIView.as_view()),
    path('delete/<int:pk>/', views.TaskDestroyAPIView.as_view()),

    # send task
    path('send-task/list/', views.SendTaskListAPIView.as_view()),
    path('send-task/create/', views.SendTaskCreateAPIView.as_view()),

    # comment
    path('comment-detail/<int:pk>/', views.CommentDetailAPIView.as_view()),
    path('comment-list/', views.CommentListAPIView.as_view()),
    path('comment-create/', views.CommentCreateAPIView.as_view()),
]
