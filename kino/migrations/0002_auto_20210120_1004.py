# Generated by Django 3.1.5 on 2021-01-20 08:04

from django.db import migrations, models
import django.db.models.deletion
import kino.models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(default='', help_text='Дайте название кинотеатру.', max_length=50)),
                ('description', models.TextField(default='', help_text='Опишите кинотеатр, его расположение и/или историю.')),
                ('preview', models.ImageField(default='', help_text='Выберите превью к кинотеатру.', upload_to='cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shares_name', models.CharField(default='', help_text='Дайте название акции.', max_length=50)),
                ('description', models.TextField(default='', help_text='Опишите условия акции.')),
                ('preview', models.ImageField(default='', help_text='Выберите превью к акции.', upload_to='shares_and_disconts')),
            ],
        ),
        migrations.RemoveField(
            model_name='film',
            name='image',
        ),
        migrations.AddField(
            model_name='film',
            name='preview',
            field=models.ImageField(default='', help_text='Выберите превью к фильму.', upload_to='films'),
        ),
        migrations.AlterField(
            model_name='film',
            name='country',
            field=models.CharField(default='', help_text='Страна съемки...', max_length=100),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(default='', help_text='Опишите фильма или мультфильма.'),
        ),
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.CharField(default='', help_text='Режисер...', max_length=65),
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(default='', help_text='Жанр...', max_length=200),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(default='', help_text='Напишите название фильма или мультфильма.', max_length=100),
        ),
        migrations.CreateModel(
            name='FilmImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to=kino.models.upload_film_gallery)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kino.film')),
            ],
        ),
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinemahall_name', models.CharField(default='', help_text='Дайте название залу.', max_length=50)),
                ('description', models.TextField(default='', help_text='Опишите зал.')),
                ('preview', models.ImageField(default='', help_text='Выберите превью к залу.', upload_to='cinema_halls')),
                ('cinema', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kino.cinema')),
            ],
        ),
    ]
