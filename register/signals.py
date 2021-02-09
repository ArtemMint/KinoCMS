from django.db.models.signals import post_save
from django.contrib.auth.models import User
from register.models.client import Client


def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)

post_save.connect(create_client, sender=User)