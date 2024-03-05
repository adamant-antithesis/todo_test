from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class Status(models.TextChoices):
        OPEN = 'Open'
        IN_PROGRESS = 'In Progress'
        IN_REVIEW = 'In Review'
        ON_HOLD = 'On Hold'
        RESOLVED = 'Resolved'
        CLOSED = 'Closed',

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def assigned_user(self):
        if self.assigned_to:
            return self.assigned_to.username
        else:
            return
