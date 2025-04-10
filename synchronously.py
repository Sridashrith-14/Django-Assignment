from django.db import models
from django.conf import settings

#Signals import
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save, post_save
)

# Create your models here.
User = settings.AUTH_USER_MODEL
@receiver(pre_save, sender=User)
def user_pre_save_receiver(sender, instance, *args, **kwargs):
    print(instance.username , instance.id)

@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance,created, *args, **kwargs):
    if created:
        print("send email to ", instance.username)
        instance.save()
    else:
        print(instance.username, " just saved")