# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from register.models.client import Client


# @receiver(post_save, sender=User)
# def create_client(sender, instance, created, **kwargs):
#     if created:
#         Client.objects.create(user=instance, address=None, num_card=None,
#                               birth_date=None, gender=None, language=None, city=None)


# @receiver(post_save, sender=User)
# def update_client(sender, instance, **kwargs):
#     instance.client.save()
