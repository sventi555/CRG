from django.db import models
from datetime import date


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-order',
                    'name',
                    ]

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    class Meta:
        verbose_name_plural = 'Subcategories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    preview = models.TextField(blank=True, null=True)
    endnotes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    featured = models.BooleanField(default=False)

    @property
    def textdump(self):
        return f'{self.title} {self.content} {self.date} {self.author} {self.subcategory}'

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to=f'{date.today().year}/{date.today().month}/{date.today().day}')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images', null=True)

    def __str__(self):
        return f'https://crgreview.com/media/{self.image.name}'


class StatusUpdate(models.Model):
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.content[0:10] + '...'





