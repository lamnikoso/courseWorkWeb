# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 09:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTaken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateField(verbose_name='Дата взятия')),
                ('date_pass', models.DateField(verbose_name='Дата сдачи')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('list_books_favorites', models.ManyToManyField(blank=True, related_name='profile_list_books_favorites', to='book.Book', verbose_name='Список избранных книг')),
                ('list_books_taken', models.ManyToManyField(through='user.BookTaken', to='book.Book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booktaken',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
        ),
    ]
