from django.db import models
from django.urls import reverse

from config.settings import AUTH_USER_MODEL
from ..team_user.models import Account, Group

STATUS = (
    (0, 'NEW'),
    (1, 'PROCESS'),
    (2, 'FINISHED'),
    (3, 'CANCELED'),
)
PRIORITY = (
    (0, 'NONE'),
    (1, 'LOW'),
    (2, 'MEDIUM'),
    (3, 'HIGH'),
)


class Task(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    supervisor = models.BooleanField(default=False)
    superuser = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='Manager')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    deadline = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


class SendTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='sender')
    receiver = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='receiver')
    message = models.CharField(max_length=500, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.sender


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
