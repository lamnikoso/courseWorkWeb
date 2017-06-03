from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from book.models import Book

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, verbose_name="Адрес")
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    list_books_taken = models.ManyToManyField(Book, through='BookTaken')
    list_books_favorites = models.ManyToManyField(Book, verbose_name='Список избранных книг', related_name='%(class)s_list_books_favorites', blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

class BookTaken(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_taken = models.DateField(verbose_name='Дата взятия')
    date_pass = models.DateField(verbose_name='Дата сдачи')

    def __str__(self):
        return "Дата взятия {} и Дата сдачи {}".format(self.date_taken, self.date_pass)

    def get_date_pass(self):
        return "Необходимо сдать до {}".format(self.date_pass)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()