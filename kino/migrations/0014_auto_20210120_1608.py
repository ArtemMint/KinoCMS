# Generated by Django 3.1.5 on 2021-01-20 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0013_auto_20210120_1512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cinema',
            options={'verbose_name': 'Кинотеатр', 'verbose_name_plural': 'Кинотеатры'},
        ),
        migrations.AlterModelOptions(
            name='cinemagallery',
            options={'verbose_name': 'Галерея кинотеатра', 'verbose_name_plural': 'Галереи кинотеатров'},
        ),
        migrations.AlterModelOptions(
            name='cinemahall',
            options={'verbose_name': 'Залы кинотеатра', 'verbose_name_plural': 'Залы кинотеатров'},
        ),
        migrations.AlterModelOptions(
            name='cinemahallgallery',
            options={'verbose_name': 'Галерея залов кинотеатра', 'verbose_name_plural': 'Галереи залов кинотеатров '},
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='filmgallery',
            options={'verbose_name': 'Галерея фильма', 'verbose_name_plural': 'Галереи фильмов'},
        ),
    ]
