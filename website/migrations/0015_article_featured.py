# Generated by Django 2.1.3 on 2018-11-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20181111_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]