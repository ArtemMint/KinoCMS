# Generated by Django 3.1.5 on 2021-02-22 16:26

from django.db import migrations, models
import kino.models.cinema


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0014_auto_20210222_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemahall',
            name='preview',
            field=models.ImageField(upload_to=kino.models.cinema.upload_cinemahall_preview),
        ),
        migrations.AlterField(
            model_name='cinemahall',
            name='scheme',
            field=models.ImageField(upload_to='images/scheme'),
        ),
    ]
