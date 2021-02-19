# Generated by Django 3.1.5 on 2021-02-18 14:29

from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0003_aboutimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/advertising')),
                ('advertising', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='kino.page')),
            ],
        ),
    ]
