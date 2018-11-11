from django.contrib import admin
from .models import *

admin.site.register(StatusUpdate)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Image)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'category',
    ]

    list_display = [
        'name',
        'category',
    ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'content',
        'image',
        'author',
        'subcategory',
    ]

    list_display = [
        'title',
        'author',
        'subcategory',
    ]


