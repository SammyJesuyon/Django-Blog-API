from rest_framework import serializers
from .models import (Blog, BlogComment, BlogTag,)


class BlogTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogTag
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    #tags variable is created so that the tags on the endpoint do not show as index but the object
    #and many is set to true because one blog can have several tags
    tags = BlogTagSerializer(many=True)
    
    class Meta:
        model = Blog
        fields = '__all__'
    
class BlogCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogComment
        fields = '__all__'
    