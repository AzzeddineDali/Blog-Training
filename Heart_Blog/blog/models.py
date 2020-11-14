from django.db import models


class BlogArticle(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_to = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(default='default.jpg',  upload_to='blog-pics')

    def __str__(self):
        return self.title
