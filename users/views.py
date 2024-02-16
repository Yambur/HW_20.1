from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

import secrets
from users.forms import RegisterUserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    """def form_valid(self, form):
        user = form.save(commit=False)

        if not user.email_verified:
            token = secrets.token_urlsafe(16)
            user.activation_token = token
            user.save()

            send_mail(subject= 'Подтверждение адреса электронной почты',
                      message= f'Для подтверждения адреса электронной почты, копируйте данный пароль {token}',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[user.email]
                      )

        return super().form_valid(form)"""
