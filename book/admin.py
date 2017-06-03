from django.contrib import admin
from .models import Book, Genre, Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'count', 'status']
    ordering = ['author']
    actions = ['make_in_stock', 'make_not_available']
    search_fields = ('title',)

    def make_in_stock(self, request, queryset):
        queryset.update(count=1)
        rows_updated = queryset.update(status='y')
        if rows_updated == 1:
            message_bit = "1 book was"
        else:
            message_bit = "{} books were".format(rows_updated)
        self.message_user(request, "{} successfully marked as in stock.".format(message_bit))
    
    make_in_stock.short_decsription = "Пометить новость как есть в наличии"

    def make_not_available(self, request, queryset):
        queryset.update(count=0)
        rows_updated = queryset.update(status='n')
        if rows_updated == 1:
            message_bit = "1 book was"
        else:
            message_bit = "{} books were".format(rows_updated)
        self.message_user(request, "{} successfully marked as not availabe.".format(message_bit))

    make_not_available.short_decsription = "Пометить новость как нет в наличии"

class GenreAdmin(admin.ModelAdmin):

    list_display = ['id', 'title']
    ordering = ['title']
    search_fields = ('title',)

class AuthorAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'last_name']
    ordering = ['name', 'last_name']
    search_fields = ('name', 'last_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)