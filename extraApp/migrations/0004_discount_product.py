# Generated by Django 5.0.2 on 2024-02-28 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extraApp', '0003_discount'),
        ('mainApp', '0010_remove_product_discount_product_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.product'),
        ),
    ]
