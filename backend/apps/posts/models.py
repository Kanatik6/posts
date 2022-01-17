from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=20)
    like_rating = models.PositiveIntegerField(default=0)
    dislike_rating = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"{self.user.username}, - {self.title}"


class Like(models.Model):
    time = models.DateTimeField(auto_now_add=True,
                                verbose_name='Время создания')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Пост')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f"{self.post.title}, - {self.user.username}"


class DisLike(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='dislikes')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dislikes')

    class Meta:
        verbose_name = 'Дизлайк'
        verbose_name_plural = 'Дизлайки'

    def __str__(self):
        return f"{self.post.title}, - {self.user.username}"
