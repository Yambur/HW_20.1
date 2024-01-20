from django.core.management import BaseCommand
from django.db import connection

from django.db import reset_queries
from main.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Овощи', 'description': 'Экзотические'},
            {'name': 'Фрукты', 'description': 'Экзотические'},
            {'name': 'Овощи', 'description': 'Стандартные'},
            {'name': 'Напитки', 'description': 'Стандартные'},
        ]

        Category.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE main_category_id_seq RESTART WITH 1")

        categories_to_create = []
        for category in category_list:
            categories_to_create.append(Category(**category))

        Category.objects.bulk_create(categories_to_create)

        products_list = [
            {'name': 'Кабачок', 'description': 'Просто кабачок',
             'category': categories_to_create[2], 'price': '50'},
            {'name': 'Картошка', 'description': 'С голубыми глазками',
             'category': categories_to_create[0], 'price': '100'},
            {'name': 'Папая', 'description': 'Знать бы что это',
             'category': categories_to_create[1], 'price': '300'},
            {'name': 'Томатный сок', 'description': 'Вкусный, но не всем заходит',
             'category': categories_to_create[3], 'price': '120'},
        ]

        Product.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE main_product_id_seq RESTART WITH 1")

        products_to_create = []
        for product in products_list:
            products_to_create.append(Product(**product))

        Product.objects.bulk_create(products_to_create)
