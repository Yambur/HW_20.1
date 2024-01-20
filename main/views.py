from django.shortcuts import render

from main.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list
    }
    return render(request, 'main/index.html')
