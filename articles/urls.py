from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:article_id>', views.article, name="article"),
    path('add', views.add, name="add")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

