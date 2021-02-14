# Generated by Django 3.1.5 on 2021-02-14 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('num_card', models.CharField(max_length=20)),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('Unknown', 'Unknown'), ('Male', 'Male'), ('Female', 'Female')], default=('Unknown', 'Unknown'), max_length=20)),
                ('language', models.CharField(choices=[('ENG', 'English'), ('UA', 'Ukrainian'), ('RU', 'Russian')], default=('ENG', 'English'), max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=14, region=None, unique=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
