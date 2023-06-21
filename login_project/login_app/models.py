from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    core_categories = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
