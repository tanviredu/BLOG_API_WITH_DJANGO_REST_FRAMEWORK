from django.db import models

# Create your models here.

## here goes all the model
class Author(models.Model):
    ## create the ORM
    name = models.CharField(max_length=150)
    email = models.EmailField()

    # this will change the author objects into str
    def __str__(self):
        return self.name +" Author Id : "+str(self.id)


class Article(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author',related_name='articles',on_delete=models.CASCADE)


    def __str__(self):
        return self.title