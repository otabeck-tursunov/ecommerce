# Generated by Django 5.0.2 on 2024-03-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0015_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='Acer', max_length=255),
        ),
    ]
