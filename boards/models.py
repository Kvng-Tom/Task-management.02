from django.db import models
from django.conf import settings

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__ (self):
    
        return self.name
    

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

    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY, default='medium')
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
