from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import Product, Contact


class IndexView(TemplateView):
    template_name = 'main/index.html'
    product_list = Product.objects.all()
    extra_context = {
        'objects_list': product_list
    }


# оставил для примера
# def index(request):
#    product_list = Product.objects.all()
#    context = {
#    'objects_list': product_list
#    }
#    return render(request, 'main/index.html', context)


"""def contacts(request):
    company_info = Contact.objects.all()
    info_content = {
        'info_list': company_info
    }
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "main/contacts.html", info_content)"""


class ContactsView(TemplateView):
    template_name = "main/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_info = Contact.objects.all()
        context['info_list'] = company_info
        return context
