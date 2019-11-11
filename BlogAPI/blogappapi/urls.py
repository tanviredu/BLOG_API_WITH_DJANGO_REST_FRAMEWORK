from django.urls import path

from . import views

urlpatterns = [
    path('',views.Postlist.as_view()),
    path('<int:pk>/',views.PostDetail.as_view())
]