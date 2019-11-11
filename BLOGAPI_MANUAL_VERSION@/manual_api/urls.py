from django.urls import path,include
from . import views

urlpatterns = [
    path('all_post/',views.PostList.as_view(),name='PostList'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='PostDetail')
]
