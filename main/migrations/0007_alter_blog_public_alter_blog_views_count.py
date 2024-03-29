# Generated by Django 4.2 on 2024-02-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_blog_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='public',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='views_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Просмотры'),
        ),
    ]
