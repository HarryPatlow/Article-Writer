from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django import forms

from .models import Article
# Create your views here.

class PublishForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('thumbnail', 'title', 'content', 'author')


# class PublishForm(forms.Form):
#     thumbnail = forms.ImageField()
#     title = forms.CharField()
#     content = forms.Textarea()
#     author = forms.CharField()


def index(request):
    return render(request, 'articles/index.html',{
        "articles":Article.objects.all()
    })

def article(request, article_id):
    return render(request, "articles/article.html",{
        "article":Article.objects.get(pk=article_id)
    })


# def add(request):
# 	if request.method == "POST":
# 		form = PublishForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 		return redirect("index")

# 	form = PublishForm()
# 	return render(request=request, template_name="articles/add.html", context={'form':form})

# def add(request):
#     context = {}
#     if request.method == "POST":
#         form = PublishForm(request.POST, request.FILES)
#         if form.is_valid():
#             img = form.cleaned_data.get("thumbnail")
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             author = form.cleaned_data.get("author")
#             art = Article.objects.create(
#                                  thumbnail = img,
#                                  title = title,
#                                  content = content,
#                                  author = author
#                                  )
#             art.save()
#             print(art)
#     else:
#         form = PublishForm()
#     context['form']= form
#     return render(request, "articles/add.html", context)

def add(request):
  
    if request.method == 'POST':
        form = PublishForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PublishForm()
    return render(request, 'articles/add.html', {'form' : form})
  