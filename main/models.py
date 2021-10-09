from typing import ContextManager
from django.db import models

# Create your models here.

class Post(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = models.ImageField(blank= True, null = True)
    contents = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.postname