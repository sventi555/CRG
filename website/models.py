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


class Image(models.Model):
    image = models.ImageField(upload_to=f'{date.today().year}/{date.today().month}/{date.today().day}')

    def __str__(self):
        return f'https://domain.com/media/{self.image.name}'


# TODO: move header layout and edit font, add about page, social media links

class Article(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    # TODO: Endnotes
    # TODO: Preview
    image = models.ImageField(upload_to="thumbnails/", null=True)
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


class StatusUpdate(models.Model):
    content = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.content[0:10] + '...'





