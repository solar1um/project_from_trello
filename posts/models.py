from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE)
    post = models.TextField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    seen = models.BooleanField()
