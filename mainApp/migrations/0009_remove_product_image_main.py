# Generated by Django 5.0.2 on 2024-02-27 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_remove_product_image_sub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_main',
        ),
    ]
