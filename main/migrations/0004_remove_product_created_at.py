# Generated by Django 4.2 on 2024-01-20 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
    ]
