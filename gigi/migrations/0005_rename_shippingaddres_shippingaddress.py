# Generated by Django 4.1.3 on 2022-12-07 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gigi', '0004_customer_order_alter_feature_price_shippingaddres_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAddres',
            new_name='ShippingAddress',
        ),
    ]
