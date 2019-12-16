## before you do anything you need to know what is a  serializer
## what the database is sedning is now like the data 
## that python work with
## the main jon of the serializer is to convert it
## to a native python so we can easily transfer in to json
## we make a something exactly looks like a models

from rest_framework import serializers
from .models import Article
#class ArticleSerializer(serializers.Serializer):
#    title = serializers.CharField(max_length=150)
#    description = serializers.CharField()
#    body = serializers.CharField()

## thats it now before rendering in the views.py just feed through it

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    description = serializers.CharField()
    body = serializers.CharField()

    ## we are using the author id and it will be matched with the 
    ## author column author id
    author_id = serializers.IntegerField()

    ## for creating the data 
    ## this is the serializer syntax

    def create(self,validated_data):

        ## this validation comes from the post method 
        return Article.objects.create(**validated_data)

    ## now for update

    # def update(self,instance,validated_data):
    #     ## we send from the put method 
    #     ## the instance and the new data with validated  data

    #     ## this is a little tricky
    #     ## we get the data from the validated data
    #     ## thich is the updated data but if the user dont give the data
    #     ## it will be the previous instance data
    #     instance.title = validated_data.get('title',instance.title)
    #     instance.description = validated_data.get('description',instance.description)
    #     instance.body = validated_data.get('body',instance.body)
    #     instance.author_id = validated_data.get('author_id',instance.author_id)

    #     ## save the instance
    #     instance.save()
    #     return instance




    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance