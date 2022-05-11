from django.db import models
from django.contrib.auth.models import User


class BlogTag(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Blog(models.Model):
    tags = models.ManyToManyField(BlogTag, related_name='blog_tags')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='blog_author', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class meta:
        ordering = ("-created_at")
        
class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, related_name='blog_comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='blog_comment_author', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class meta:
        ordering = ("-created_at")