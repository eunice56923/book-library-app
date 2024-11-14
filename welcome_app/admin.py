# admin.py
from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publish_date')
    list_filter = ('category', 'publish_date')
    search_fields = ('title', 'author')
    ordering = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
