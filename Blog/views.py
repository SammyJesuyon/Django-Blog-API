from .serializers import (BlogTag, Blog, BlogComment, BlogCommentSerializer, BlogSerializer, BlogTagSerializer)
from rest_framework.viewsets import ModelViewSet


class BlogView(ModelViewSet):
    #returns all blogs when queried
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class BlogCommentView(ModelViewSet):
    #returns all blog comments when queried
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    
class BlogTagView(ModelViewSet):
    #returns all blog tags when queried
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer