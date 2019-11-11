from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

## serializer is actually a format

## we take the data dn then pipe it to the written serializer format

class Postlist(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetail(generics.RetrieveAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializer