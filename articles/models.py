from distutils.command.upload import upload
from django.db import models
# Create your models here.

class Article(models.Model):
    thumbnail = models.ImageField(upload_to = "uploads/", blank = True, null=True)
    thumbnail_url = models.CharField(max_length=1000, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=64)
    date_modified = models.DateTimeField(auto_now_add=True)
