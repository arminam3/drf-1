from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey(User, related_name='article', on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title