from django.shortcuts import render
from .models import BlogArticle


def home(request):

    articles = BlogArticle.objects.all()
    return render(request, 'blog/home.html', {"blogs": articles})


def detail(request, blog_id):

    blog_target = BlogArticle.objects.get(pk=blog_id)
    return render(request, 'blog/post.html', {"blog_target": blog_target})