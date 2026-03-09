from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    seniority = models.CharField(max_length=100)
    skills = models.TextField(blank=True)


    def __str__(self):
        return self.username
    