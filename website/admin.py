from django.contrib import admin
from .models import *

admin.site.register(StatusUpdate)
admin.site.register(Author)
admin.site.register(Image)
admin.site.register(SubmissionRequest)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'name'
    ]


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


class ImageInline(admin.TabularInline):
    model = Image
    extra = 2


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'author',
        'subcategory',
    ]

    inlines = [
        ImageInline
    ]




