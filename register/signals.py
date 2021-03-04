from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from register.models.client import Client


@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    """After creating User instance
    create empty Client 

    Args:
        sender ([type]): [description]
        instance ([type]): [description]
        created ([type]): [description]
    """
    if created:
        Client.objects.create(
            user=instance,
            address=None,
            num_card=None,
            birth_date=None,
            gender=None,
            language=None,
            phone=None,
            city=None,
        )


@receiver(post_save, sender=User)
def update_client(sender, instance, **kwargs):
    """Save Client

    Args:
        sender ([type]): [description]
        instance ([type]): [description]
    """
    instance.client.save()
