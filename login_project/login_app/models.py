from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    emailId = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class PostModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    core_categories = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')