from django.shortcuts import render
from ex11.models import User, Post, Comment


# Задание 11
def users(request):
    user = list(User.objects.all())
    return render(request, 'ex11/users.html', {"users": user})


# Задание 12
def comments_count(request):
    try:
        c = Comment.objects.all().count()
    except:
        c = None
    return render(request, 'ex11/comments_count.html', {"c": c})


# Задание 13
def post_comments(request):
    try:
        post_list = Post.objects.filter(user_id=1)
        com = []
        for p in post_list:
            com.extend(list(Comment.objects.filter(post_id=p.id).order_by('comment_date')))
    except:
        com = 0
    return render(request, 'ex11/posts_comments.html', {"com": com})


# Задание 14
def userv(request):
    try:
        user = User.objects.get(id=100)
    except:
        user = None
    return render(request, 'ex11/user.html', {"user": user})


# Задание 15
def postsfirst(request):
    try:
        post = Post.objects.filter(user_id=1).order_by('post_date')[0:10]
    except:
        post = None
    return render(request, 'ex11/postsfirst.html', {"post": post})