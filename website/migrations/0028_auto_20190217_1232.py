# Generated by Django 2.1.7 on 2019-02-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_auto_20181117_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='2019/2/17'),
        ),
    ]