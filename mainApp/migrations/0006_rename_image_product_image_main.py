# Generated by Django 5.0.2 on 2024-02-27 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image_main',
        ),
    ]
