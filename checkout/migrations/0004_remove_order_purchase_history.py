# Generated by Django 3.2.6 on 2021-09-27 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210916_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='purchase_history',
        ),
    ]
