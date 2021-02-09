# Generated by Django 3.1.5 on 2021-02-02 15:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from kino.models.shares import *


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0035_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('address', models.TextField(blank=True)),
                ('status', models.BooleanField(default=False)),
                ('latitude', models.FloatField(max_length=50)),
                ('longitude', models.FloatField(max_length=50)),
                ('logo', models.ImageField(upload_to=upload_shares_preview)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
                ('status', models.BooleanField(default=False)),
                ('preview', models.ImageField(upload_to=upload_shares_preview)),
                ('image1', models.ImageField(blank=True, null=True, upload_to=upload_shares_gallery)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=upload_shares_gallery)),
                ('image3', models.ImageField(blank=True, null=True, upload_to=upload_shares_gallery)),
                ('image4', models.ImageField(blank=True, null=True, upload_to=upload_shares_gallery)),
                ('image5', models.ImageField(blank=True, null=True, upload_to=upload_shares_gallery)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.CharField(blank=True, max_length=14, null=True)),
                ('phone2', models.CharField(blank=True, max_length=14, null=True)),
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kino.pagemodel')),
            ],
        ),
    ]
