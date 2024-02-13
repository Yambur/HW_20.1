from django import forms

from main.models import Product, Version


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active_version':
                field.widget.attrs['class'] = 'form-control'


class VersionForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'category', 'price',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Введено запрещенное к использованию слово')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Название продукта не может содержать слово "{word}"')

        return cleaned_data
