from django.shortcuts import render

from .models import Article
# Create your views here.


def index(request):
    return render(request, 'articles/index.html',{
        "articles":Article.objects.all()
    })

def article(request, article_id):
    return render(request, "articles/article.html",{
        "article":Article.objects.get(pk=article_id)
    })

def add(request):
    return render(request, "articles/editor.html")