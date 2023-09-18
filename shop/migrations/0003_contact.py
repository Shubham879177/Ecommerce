# Generated by Django 4.2.5 on 2023-09-18 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=12)),
            ],
        ),
    ]