from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView

from main.models import Product, Contact, Blog


class IndexView(TemplateView):
    template_name = 'main/index.html'
    product_list = Product.objects.all()
    extra_context = {
        'objects_list': product_list
    }


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


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'message')
    success_url = reverse_lazy('main:blog')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class BlogUpdateView(UpdateView):
    pass
