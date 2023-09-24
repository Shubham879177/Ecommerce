# Generated by Django 4.2.5 on 2023-09-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(default='', max_length=300)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=300)),
                ('city', models.CharField(default='', max_length=30)),
                ('state', models.CharField(default='', max_length=30)),
                ('zip', models.IntegerField(default='', max_length=7)),
                ('phone', models.IntegerField(default='', max_length=11)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
    ]
