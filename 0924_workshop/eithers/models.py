from django.db import models
from django.conf import settings


class Either(models.Model):
    title = models.CharField(max_length=10)
    topic = models.CharField(max_length=200)
    content_left = models.TextField()
    content_right = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    CHOICE = [
        ('LEFT', 'left'),
        ('RIGHT', 'right'),
    ]
    either = models.ForeignKey(Either, on_delete=models.CASCADE)
    vote = models.CharField(max_length=5, choices=CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content