# Generated by Django 4.2 on 2024-02-19 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_verified_user_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.CharField(default='eebaqWk', max_length=10, verbose_name='Код вeрификации'),
        ),
    ]
