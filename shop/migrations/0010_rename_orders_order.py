# Generated by Django 4.2.5 on 2023-09-24 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orders_delete_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
