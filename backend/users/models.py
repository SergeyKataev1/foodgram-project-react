from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.validators import ValidationError


class CustomUser(AbstractUser):

    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):

    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             verbose_name='Подписчик',
                             related_name='subscriber')
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               verbose_name='Автор',
                               related_name='author')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='subscribe_unique'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def clean(self):
        if self.user == self.author:
            raise ValidationError('error: Подписка на самого себя запрещена')

    def __str__(self):
        return f'{self.user} добавил "{self.author}"в подписки'
