from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import (
    user_signed_up, user_logged_in, password_changed)

from django.contrib.auth.models import User


class CustomerAccount(models.Model):
    """
   A model for storing customer contact details
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(
        max_length=80, null=True, blank=True)
    phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(
        max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_customer_account(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        CustomerAccount.objects.create(user=instance)

    instance.customeraccount.save()


@receiver(user_logged_in)
def check_if_superuser(sender, request, user, **kwargs):
    """
    Check if user is super user and delete session variable to prevent basket items causing 404 error when deleted from db
    """
    if request.user.is_superuser:
        # try/catch block to prevent keyerror if no basket exists for super user
        try:
            del request.session['basket']
            request.session.modified = True
        except Exception as e:
            pass
