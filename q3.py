# models.py

from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

class UserAccount(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class EmailLog(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

@receiver(post_save, sender=UserAccount)
def welcome_email_handler(sender, instance, created, **kwargs):
    if created:
        try:
            # Simulate creating an email log entry
            EmailLog.objects.create(user=instance, status='Sending')
            # Simulate error while sending email
            raise Exception("Failed to send welcome email")
        except Exception as e:
            logging.error("Signal error: %s", str(e))
