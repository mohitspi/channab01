# Generated by Django 3.0.8 on 2020-07-15 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_category_instance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
