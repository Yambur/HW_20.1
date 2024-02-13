from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from pytils.translit import slugify

from main.forms import ProductForm, VersionForm
from main.models import Product, Contact, Blog, Category, Version


class IndexView(TemplateView):
    template_name = 'main/index.html'
    product_list = Product.objects.all()
    extra_context = {
        'objects_list': product_list,
    }


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории продуктов'
    }


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data()
        products = Product.objects.filter(category=self.object)
        context_data['title'] = 'Продукты категории'
        context_data['products'] = products
        return context_data


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset



class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:category_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:category_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:category_list')


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
    extra_context = {
        'title': 'Личный блог'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(public=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'message')
    success_url = reverse_lazy('main:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'message')
    success_url = reverse_lazy('main:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('main:blog')


def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.public:
        blog_item.public = False
    else:
        blog_item.public = True

    blog_item.save()
    return redirect(reverse('main:blog'))
