from django.shortcuts import render
from .models import BlogArticle
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogArticle


class PostListView(ListView):
    model = BlogArticle
    template_name = 'blog/home.html'
    context_object_name = 'blogs'


class PostDetailView(DetailView):
    model = BlogArticle


class PostCreateView(CreateView):
    model = BlogArticle
    fields = ['title', 'description', 'image']
    
