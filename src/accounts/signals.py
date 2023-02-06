from django.db.models.signals import post_save
from django.dispatch import receiver

from src.accounts.models import User, Profile


@receiver(post_save, sender=User)
def profile_created(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

