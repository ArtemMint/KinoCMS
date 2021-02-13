# Generated by Django 3.1.5 on 2021-02-12 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='FilmImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.film')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
