from django.contrib import admin
from django.urls import path
from . import views

## you have to invoke the as_view() always
urlpatterns = [
    path('articles/',views.ArticleView.as_view()),
    path('articles/<int:pk>/',views.ArticleView.as_view()),
    ## the url you enterd will be exactly ike that
    path('articles/read/<int:pk>/',views.readArticle.as_view())
]
