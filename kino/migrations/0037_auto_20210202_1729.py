# Generated by Django 3.1.5 on 2021-02-02 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0036_contactmodel_homepagemodel_pagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagemodel',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.pagemodel'),
        ),
    ]