from django.db import models

from apps.team_user.models import Account


class Chat(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='Sender')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Receiver')
    message = models.CharField(max_length=600)
    is_read = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.sender.first_name:
            return self.sender.first_name
        return f'{self.sender.email}'

