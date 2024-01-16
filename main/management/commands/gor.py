from django.core.management import BaseCommand
from django.db import connection

from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Овощи', 'description': 'Экзотические'},
            {'name': 'Фрукты', 'description': 'Экзотические'},
            {'name': 'Овощи', 'description': 'Стандартные'},
            {'name': 'Напитки', 'description': 'Стандартные'},
        ]

        Category.objects.all().delete()

        # не могу понять, где изменять id
        #with connection.cursor() as cursor:
        #    cursor.execute("ALTER SEQUENCE category_id RESTART WITH 1")

        categories_to_create = []
        for category in category_list:
            categories_to_create.append(Category(**category))

        Category.objects.bulk_create(categories_to_create)