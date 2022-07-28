from django.urls import path
from .views import *

urlpatterns = [
    path('list/', NotificationListAPIView.as_view()),
    path('create/', NotificationCreateAPIView.as_view()),
]
