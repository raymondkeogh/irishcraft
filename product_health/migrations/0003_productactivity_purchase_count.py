# Generated by Django 3.2.6 on 2021-09-20 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_health', '0002_auto_20210831_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='productactivity',
            name='purchase_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
