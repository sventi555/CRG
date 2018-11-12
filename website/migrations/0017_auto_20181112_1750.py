# Generated by Django 2.1.3 on 2018-11-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20181111_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endnote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='preview',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='2018/11/12'),
        ),
        migrations.AddField(
            model_name='article',
            name='endnotes',
            field=models.ManyToManyField(to='website.Endnote'),
        ),
    ]
