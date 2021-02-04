# Generated by Django 3.1.5 on 2021-01-30 15:05

from django.db import migrations, models
import kino.models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0032_auto_20210130_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='image1',
            field=models.ImageField(blank=True, upload_to=kino.models.upload_shares_gallery),
        ),
        migrations.AlterField(
            model_name='shares',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=kino.models.upload_shares_gallery),
        ),
        migrations.AlterField(
            model_name='shares',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=kino.models.upload_shares_gallery),
        ),
        migrations.AlterField(
            model_name='shares',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=kino.models.upload_shares_gallery),
        ),
        migrations.AlterField(
            model_name='shares',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to=kino.models.upload_shares_gallery),
        ),
        migrations.AlterField(
            model_name='shares',
            name='preview',
            field=models.ImageField(upload_to=kino.models.upload_shares_preview),
        ),
    ]