from django.urls import path
from .views import *

urlpatterns = [
    path('create/', TodoCreateAPIView.as_view()),
    path('list/', TodoListAPIView.as_view()),
    path('rud/<int:pk>/', TodoRDAPIView.as_view()),
    path('update/<int:pk>/', TodoAPIView.as_view()),
]
