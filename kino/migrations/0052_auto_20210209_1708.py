# Generated by Django 3.1.5 on 2021-02-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0051_auto_20210209_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='coordinates',
            field=models.IntegerField(max_length=50),
        ),
    ]
