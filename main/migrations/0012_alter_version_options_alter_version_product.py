# Generated by Django 4.2 on 2024-02-10 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
    ]