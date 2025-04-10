import threading
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

User = settings.AUTH_USER_MODEL

@receiver(pre_save, sender=User)
def user_pre_save_receiver(sender, instance, *args, **kwargs):
    print("PRE_SAVE: Username:", instance.username)
    print("PRE_SAVE: Signal running in thread:", threading.current_thread().name)

@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("POST_SAVE: Username:", instance.username)
    print("POST_SAVE: Signal running in thread:", threading.current_thread().name)
