from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='user'),  # задание 11
    path('comments/', views.comments_count, name ='comment'), # задание 12
    path('posts/comments/', views.post_comments, name ='comment'),  # задание 13
    path('user/', views.userv, name='user'),  # задание 14
    path('postsfirst/', views.postsfirst, name='post'),  # задание 15
]
