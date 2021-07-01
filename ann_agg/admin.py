from django.contrib import admin

from ann_agg.models import Author, Book, Publisher, Store


class BookInline(admin.TabularInline):
    model = Book
    extra = 2


class PublisherAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [BookInline]
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Publisher, PublisherAdmin)
