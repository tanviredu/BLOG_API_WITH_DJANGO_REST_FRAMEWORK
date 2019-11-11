from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Post

def all_post(request):
    posts = Post.objects.all()[:5]

    ## extract the value we needned and 
    ## put then unnder result dicy and make a total json
    data = {"results": list(posts.values("user", "title", "content","created_at","updated_at"))}
    return JsonResponse(data)


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    data = {
        "results":{
            "title":post.title,
            "content":post.content,
            "created_at":post.created_at,
            "updated_at":post.updated_at
        }
        
    }
    return JsonResponse(data)


