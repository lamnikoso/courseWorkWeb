from django.db import models
from django.conf import settings

# Create your models here.
STATUS_CHOICES = (
    ('y', 'Есть в наличии'),
    ('n', 'Нет в наличии'),
)

class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Author(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    bio = models.TextField(verbose_name='Биография')

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр', blank=True)
    annotation = models.TextField(verbose_name='Аннотация')
    img = models.ImageField(upload_to='img/', default = '/img/no-img.jpg')
    receipt_date = models.DateField(verbose_name='Дата поступления')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Статус')
    count = models.PositiveSmallIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return "Название {}, автор {}, Дата поступления {}".format(self.title, self.author, self.receipt_date)

    def get_status(self):
        if self.status == 'y':
            return "Есть в наличии"
        elif self.status == 'n':
            return "Нет в наличии"

    def get_count(self):
        return self.count

    def save(self, *args, **kwargs):
        if self.count > 0:
            self.status = 'y'
        elif self.count == 0:
            self.status = 'n'
        super(Book, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'