from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('posts/', PostList.as_view(), name="posts"),
    path('post/<pk>/', PostDetailView.as_view(), name="post_detail"),

]