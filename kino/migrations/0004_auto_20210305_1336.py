# Generated by Django 3.1.5 on 2021-03-05 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0003_auto_20210305_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='three_dimension',
            new_name='three_dimensions',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='two_dimension',
            new_name='two_dimensions',
        ),
    ]
