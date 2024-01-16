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
