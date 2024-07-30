from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    task = models.TextField()
    created_at = models.DateField()
    
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task

class Profile(models.Model):
    title = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="profile_pic/")

