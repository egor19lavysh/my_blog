from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    publishing_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

