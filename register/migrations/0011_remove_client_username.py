# Generated by Django 3.1.5 on 2021-02-04 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20210204_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='username',
        ),
    ]
