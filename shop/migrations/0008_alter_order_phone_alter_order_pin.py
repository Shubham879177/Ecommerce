# Generated by Django 4.2.5 on 2023-09-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_zip_order_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='order',
            name='pin',
            field=models.CharField(default='', max_length=7),
        ),
    ]
