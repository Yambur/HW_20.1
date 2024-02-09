from django import forms

from main.models import Product


class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        #fields = '__all__'
        fields = ('name', 'description', 'category', 'price',)
