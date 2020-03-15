from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    assignee = models.TextField()
    completed = models.BooleanField(default=False)

