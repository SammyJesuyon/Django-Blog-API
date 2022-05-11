from rest_framework import serializers
from .models import (Blog, BlogComment, BlogTag,)


class BlogSerializer(serializers.ModelSerializer):
    
    class meta:
        model = Blog
        fields = '__all__'
    
class BlogCommentSerializer(serializers.ModelSerializer):
    
    class meta:
        model = BlogComment
        fields = '__all__'
    
class BlogTagSerializer(serializers.ModelSerializer):
    
    class meta:
        model = BlogTag
        fields = '__all__'