# Generated by Django 3.0.8 on 2020-08-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200801_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addedanimallivestock',
            name='female_parent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='addedanimallivestock',
            name='male_parent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='parentschild',
            name='child_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
