# Generated by Django 5.0.2 on 2024-02-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_productproperty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productproperty',
            name='context',
            field=models.TextField(),
        ),
    ]
