from django.db import models
from django.conf import settings

# Create your models here.


class Tasks(models.Model) :

    STATUS = [
        ('todo', 'To Do'),
        ('in-progress', 'In Progress'),
        ('done', 'Done'),
    ]

    PRIORITY = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY, default='medium')
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
