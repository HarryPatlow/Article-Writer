from django.contrib import admin

from .models import Article

from django.utils.html import format_html
# Register your models here.

@admin.register(Article) 
class ArticleAd(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:70px; height:80px; object-fit:cover" />'.format(obj.thumbnail.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag','title','author','date_modified']
