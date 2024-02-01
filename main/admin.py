from django.contrib import admin

from main.models import Category, Product, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date_create', 'public')
    list_filter = ('date_create', 'public')
    search_fields = ('name', 'body')
