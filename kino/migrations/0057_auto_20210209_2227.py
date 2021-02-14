# Generated by Django 3.1.5 on 2021-02-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0056_auto_20210209_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharesbanner',
            name='spin_speed',
        ),
        migrations.AlterField(
            model_name='backbanner',
            name='image',
            field=models.ImageField(upload_to='banners/back'),
        ),
        migrations.AlterField(
            model_name='sharesbanner',
            name='image',
            field=models.ImageField(upload_to='banners/shares'),
        ),
        migrations.AlterField(
            model_name='sliderbanner',
            name='image',
            field=models.ImageField(upload_to='banners/slider'),
        ),
    ]
