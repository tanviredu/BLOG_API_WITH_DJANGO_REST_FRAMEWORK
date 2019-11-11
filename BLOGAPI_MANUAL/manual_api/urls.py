from django.urls import path,include
from . import views

urlpatterns = [
    path('all_post/',views.all_post,name='all_post'),
    path('post/<int:pk>/',views.post_detail,name='post_detail')
]
