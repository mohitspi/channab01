# Generated by Django 3.0.8 on 2020-07-31 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addedanimallivestock',
            name='female_parent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='addedanimallivestock',
            name='male_parent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
