from django.urls import path
from .views import *


urlpatterns = [
    path('list/', ChatListAPIView.as_view()),
    path('create/', ChatCreateAPIView.as_view()),
]
