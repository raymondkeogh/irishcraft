# Generated by Django 3.2.6 on 2021-09-27 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_remove_order_purchase_history'),
        ('product_health', '0003_productactivity_purchase_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchaseHistory',
        ),
    ]
