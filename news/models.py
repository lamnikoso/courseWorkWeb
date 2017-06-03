# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('d', 'Черновик'),
    ('p', 'Опубликовано'),
    ('w', 'В корзине'),
)

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание')
    body = models.TextField(verbose_name='Содержание')
    publication_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    like = models.IntegerField(verbose_name='Нравиться', default=0)
    viewing = models.IntegerField(verbose_name='Просмотрено', default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Статус')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, verbose_name='Автор')
    list_users_like = models.ManyToManyField(User, verbose_name='Список пользователей, которым нравится новость', related_name='%(class)s_list_users_like', null=True, blank=True)

    def __str__(self):
        return "Название {}, автор {}, Дата публикации {}".format(self.title, self.author, self.publication_date)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
