# Generated by Django 4.2 on 2024-02-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_blog_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='public',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
