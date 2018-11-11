# Generated by Django 2.1.3 on 2018-11-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20181111_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='images',
        ),
        migrations.AddField(
            model_name='article',
            name='footnotes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='articles',
            field=models.ManyToManyField(to='website.Article'),
        ),
    ]
