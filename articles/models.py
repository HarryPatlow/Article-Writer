from distutils.command.upload import upload
from django.db import models
from matplotlib.image import thumbnail

# Create your models here.

class Article(models.Model):
    thumbnail = models.ImageField(upload_to = "uploads/", blank = True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=64)
