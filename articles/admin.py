from django.contrib import admin
import os
from .models import Article
from pathlib import Path
from django.utils.html import format_html
# Register your models here.

BASE_DIR = Path(__file__).resolve().parent.parent

@admin.register(Article) 
class ArticleAd(admin.ModelAdmin):

    def image_tag(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="width:70px; height:80px; object-fit:cover" />'.format(obj.thumbnail.url))
        elif obj.thumbnail_url:
            return format_html('<img src="{}" style="width:70px; height:80px; object-fit:cover" />'.format(obj.thumbnail_url))
        else:
            return format_html('<img src="https://acadianakarate.com/wp-content/uploads/2017/04/default-image-620x600.jpg" style="width:70px; height:80px; object-fit:cover" />')

    image_tag.short_description = 'Image'

    list_display = ['image_tag','title','author','date_modified']
