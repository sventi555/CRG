# Generated by Django 2.1.2 on 2018-11-18 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20181114_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='2018/11/17'),
        ),
        migrations.AlterField(
            model_name='statusupdate',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]
