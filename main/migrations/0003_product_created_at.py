# Generated by Django 4.2 on 2024-01-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='туфта'),
        ),
    ]
