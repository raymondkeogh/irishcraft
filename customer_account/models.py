from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    email = models.EmailField(max_length=70, blank=True, unique=True)
  
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
