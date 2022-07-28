from django.db import models

from apps.team_user.models import Account
from config.settings import AUTH_USER_MODEL


class Todo(models.Model):
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

    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




