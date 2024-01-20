from django.shortcuts import render

from main.models import Product, Contact


def index(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list
    }
    return render(request, 'main/index.html', context)


def contacts(request):
    company_info = Contact.objects.all()
    info_content = {
        'info_list': company_info
    }
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "main/contacts.html", info_content)
