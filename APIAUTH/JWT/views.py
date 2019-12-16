from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializer import ArticleSerializer

# Create your views here.


## now we have to make all the endpoint


## now this is a html response if you want 
## API response you need to write all the method
## inside a class that is inherited by API CLASS
## all the method exactly like the same just indire the class
## and you have to use the as_view() for rendering this

class ArticleView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response({'articles':serializer.data})

    ## we can actualy create a POST method here 
    ## but before doing that some sppech must be helpful
    ## we ignores the author in the serializers
    ## to make this POst method and the serializer work
    ## with the author we need to add the author_id into the 
    ## serializer
    ## and we need to create a 'create' method 
    ## inside the seriaze class to save the  data after serialize

    def post(self,request):
        article = request.data.get('article') ## get data from the article

        serializer = ArticleSerializer(data=article)
        ## now check for validation_
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            ## save it but also take the data which is saved
            ## now response it
        return Response({"success":article_saved})

    ## so thr post option is when we work with the 
    ## post we age the data from the article in a json
    ## then serialize the data
    #3 and save and validate and then save insede the model in the 
    ## create function and then send the response


    ## now put method
    ## we need the article numbber to edit we get it from the url

    # def put(self,request,pk):
    #     ## find the object
    #     saved_article = get_object_or_404(Article.objects.all(),pk=pk)

    #     ## now get the updated data
    #     data = request.data.get('article')
    #     ##send to the serializer
    #     serializer  = ArticleSerializer(instance=saved_article,data=data,partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success":article_saved})
        
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})

    def delete(self,request,pk):
        ## get the object with this pk
        article = get_object_or_404(Article.objects.all(),pk=pk)
        article.delete()
        return Response({"messgae":"the  article is deleted succesfully" })

class readArticle(APIView):
    
    def get(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        serializer = ArticleSerializer(article)
        return Response({'articles':serializer.data})
