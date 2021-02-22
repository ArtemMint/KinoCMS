# Generated by Django 3.1.5 on 2021-02-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0005_auto_20210220_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50, null=True, verbose_name='Genre:')),
            ],
        ),
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='kino.Genre'),
        ),
    ]