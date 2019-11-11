from rest_framework import serializers
## this willbe used in for processing the database 
## with JSON
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Post
        #3 we are exposing all the database infor 
        ## with a this mormat in serializer 
        ### now we create the viwe