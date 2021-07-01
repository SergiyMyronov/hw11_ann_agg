from ann_agg.models import Author, Book, Publisher, Store

from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'age']}),
    ]
    list_display = ['name', 'age', ]
    search_fields = ['name']


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'pages', 'price', 'rating', 'pubdate', 'publisher', 'authors']}),
    ]
    filter_horizontal = ('authors',)
    list_display = ['name', 'publisher', ]
    list_filter = ['publisher', 'authors']
    search_fields = ['name']


class BookInline(admin.TabularInline):
    model = Book
    extra = 2


class PublisherAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [BookInline]
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class StoreAdmin(admin.ModelAdmin):
    filter_horizontal = ('books',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Store, StoreAdmin)
