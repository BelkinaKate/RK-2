from django.db import models


class User(models.Model):
    username = models.CharField('Имя пользователя', max_length=200)
    email = models.CharField('Почта', max_length=200)
    birthday = models.DateField('Дата рождения')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post_title = models.CharField('Заголовок поста', max_length=200)
    post_text = models.CharField('Текст поста', max_length=1000)
    post_date = models.DateField('Дата публикации')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_title = models.CharField('Заголовок комментария', max_length=200)
    comment_text = models.CharField('Текст комментария', max_length=500)
    comment_date = models.DateField('Дата публикации')
