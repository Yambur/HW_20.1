from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='категория')
    description = models.TextField(max_length=300, verbose_name='описание')

    def __str__(self):
        return f'{self.name}{self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=300, verbose_name='описание')
    image = models.ImageField(upload_to='main', **NULLABLE, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    data_create = models.DateTimeField(**NULLABLE, verbose_name='дата создания')
    data_last_add = models.DateTimeField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description}{self.image}{self.category}{self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название компании", **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    email = models.CharField(max_length=200, verbose_name='Имейл', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name}: {self.phone}, {self.email},"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name="Заголовок", **NULLABLE)
    slug = models.CharField(max_length=100, verbose_name="slug", **NULLABLE)
    message = models.TextField(max_length=200, verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(upload_to='main/', **NULLABLE, verbose_name="Фото")
    date_create = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    public = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')


    def __str__(self):
        return f'{self.name} {self.message} {self.views_count}'
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

