# Generated by Django 3.1.5 on 2021-02-18 18:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0005_auto_20210218_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('time', models.TimeField(default=django.utils.timezone.now, null=True)),
                ('cinemahall', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='kino.cinemahall')),
                ('film', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='kino.film')),
            ],
        ),
    ]