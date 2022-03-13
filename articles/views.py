from django.shortcuts import render, redirect
from django import forms
from matplotlib.image import thumbnail

from .models import Article
# Create your views here.
#WORKING FORM
class PublishForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('thumbnail_url', 'title', 'content', 'author')


if len(Article.objects.all())<4:
    last3 = Article.objects.all()
else:
    last3 = Article.objects.all()[len(Article.objects.all())-3:len(Article.objects.all())]

def index(request):
    return render(request, 'articles/index.html',{
        "articles":Article.objects.all(),
        "last3": last3
    })

def article(request, article_id):
    return render(request, "articles/article.html",{
        "article":Article.objects.get(pk=article_id),
        "last3": last3
    })


def add(request):
	if request.method == "POST":
		form = PublishForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("index")

	form = PublishForm()
	return render(request=request, template_name="articles/add.html", context={'form':form,"last3": last3})


  