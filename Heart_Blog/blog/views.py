from django.shortcuts import render
from .models import BlogArticle


def home(request):

    articles = BlogArticle.objects.all()
    return render(request, 'blog/home.html', {"blogs": articles})


def detail(request):
    return render(request, 'blog/detail.html')