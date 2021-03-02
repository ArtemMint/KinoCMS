# Generated by Django 3.1.5 on 2021-03-02 05:39

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/ads')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='HallType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('seats', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), size=None)),
            ],
        ),
    ]
