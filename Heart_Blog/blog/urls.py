from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home-page'),
    path('post/<int:blog_id>/', views.detail, name='post')
]