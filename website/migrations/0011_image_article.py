# Generated by Django 2.1.3 on 2018-11-11 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_article_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Article'),
        ),
    ]
