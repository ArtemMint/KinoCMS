# Generated by Django 3.1.5 on 2021-03-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0004_auto_20210305_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='duration',
            field=models.TimeField(null=True, verbose_name='Duration of film:'),
        ),
    ]
