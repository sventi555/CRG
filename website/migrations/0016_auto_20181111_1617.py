# Generated by Django 2.1.3 on 2018-11-11 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_article_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-order', 'name'], 'verbose_name_plural': 'Categories'},
        ),
    ]
