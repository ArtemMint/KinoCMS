from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from register.models import Client


@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_client(sender, instance, **kwargs):
    instance.client.save()
