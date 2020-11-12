from django.db import models


class BlogArticle(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog-pics')

    def __str__(self):
        return self.title
