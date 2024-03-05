from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class Status(models.TextChoices):
        OPEN = 'Open', 'Відкрито'
        IN_PROGRESS = 'In Progress', 'В процесі'
        IN_REVIEW = 'In Review', 'У ревью'
        ON_HOLD = 'On Hold', 'Утримується'
        RESOLVED = 'Resolved', 'Вирішено'
        CLOSED = 'Closed', 'Закрито'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
