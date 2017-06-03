from django.contrib import admin
from .models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'publication_date', 'status']
    ordering = ['publication_date']
    actions = ['make_published', 'make_withdrawn', 'make_draft']
    search_fields = ('title', )

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "{} stories were".format(rows_updated)
        self.message_user(request, "{} successfully marked as published.".format(message_bit))
    
    make_published.short_decsription = "Пометить новость как опобликованная"

    def make_withdrawn(self, request, queryset):
        rows_updated = queryset.update(status='w')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "{} stories were".format(rows_updated)
        self.message_user(request, "{} successfully marked as withdrawn.".format(message_bit))
    
    make_withdrawn.short_decsription = "Пометить новость как удаленная"

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status='d')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "{} stories were".format(rows_updated)
        self.message_user(request, "{} successfully marked as draft.".format(message_bit))
    
    make_draft.short_decsription = "Пометить новость как черновик"
    make_draft.verbose_name = "Пометить новость как черновик"

admin.site.register(News, NewsAdmin)