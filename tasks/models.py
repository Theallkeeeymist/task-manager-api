from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=255) #title of my task
    description=models.TextField(blank=True) #description of my task
    completed=models.BooleanField(default=False) #Task done or not done
    created_at=models.DateTimeField(auto_now_add=True) #auto add timestamp of when created

    def __str__(self): #We do it for easier readability of in django admin and easier debugging
        return self.title

    # ALWAYS DEFINE __str()__ FOR EVERY DJANGO MODEL THAT WE CREATE