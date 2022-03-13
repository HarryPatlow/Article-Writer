from distutils.command.upload import upload
from django.db import models
# Create your models here.

class Article(models.Model):
<<<<<<< HEAD
    thumbnail = models.ImageField(upload_to = "uploads/", blank = True, null=True)
    thumbnail_url = models.CharField(max_length=1000, blank=True)
=======
    thumbnail = models.ImageField(upload_to = "media/uploads/", blank = True)
>>>>>>> 9c27367d7753477c2f91a6e16cdab38e5067b60e
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=64)
    date_modified = models.DateTimeField(auto_now_add=True)
