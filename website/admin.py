from django.contrib import admin
from .models import *

admin.site.register(StatusUpdate)
admin.site.register(Author)
admin.site.register(Category)


class AuthorInline(admin.TabularInline):
    model = Author


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'content',
        'image',
        'author',
        'category',
    ]

    inline = [
        AuthorInline,
        CategoryInline,
    ]

    list_display = [
        'title',
        'author',
        'category',
    ]


