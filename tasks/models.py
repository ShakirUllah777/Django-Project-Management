from django.db import models
from projects.models import Project
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOICES  = [
        ('todo', 'Todo'),
        ('progress', 'In Progress'),
        ('done', 'Completed'),
    ]

    PRIORITY_CHOICES  = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigend_to = models.ForeignKey(User,on_delete=models.CASCADE)

    start_date = models.DateField()
    due_date = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES,default='medium')


    def __str__(self):
        return self.title

