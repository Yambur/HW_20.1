from django import forms

from main.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = '__all__'
        fields = ('name', 'description', 'category', 'price',)


    """def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in name.lower():
                self.add_error('name', f'Название продукта не может содержать слово "{word}"')
            if word in description.lower():
                self.add_error('description', f'Описание продукта не может содержать слово "{word}"')

        return cleaned_data"""
