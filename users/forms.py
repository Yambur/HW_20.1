from django.contrib.auth.forms import UserCreationForm

from main.forms import StyleForMixin
from users.models import User


class RegisterUserForm(StyleForMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')