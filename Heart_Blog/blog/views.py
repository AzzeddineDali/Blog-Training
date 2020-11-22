from django.urls import reverse_lazy
from django.shortcuts import render
from .models import BlogArticle
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


# Show all posts
class PostListView(ListView):
    model = BlogArticle
    template_name = 'blog/home.html'
    context_object_name = 'blogs'


# Show one post
class PostDetailView(DetailView):
    model = BlogArticle


# Create a new post
class PostCreateView(CreateView):
    model = BlogArticle
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('home-page')


# Update Post
class PostUpdateView(UpdateView):
    model = BlogArticle
    fields = ['title', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home-page')


# Delete a post
class PostDeleteView(DeleteView):
    model = BlogArticle
    success_url = reverse_lazy('home-page')