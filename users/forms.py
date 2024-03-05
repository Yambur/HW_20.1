from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from main.forms import StyleForMixin
from users.models import User


class RegisterUserForm(StyleForMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleForMixin, UserChangeForm):
    pass

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'country', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()