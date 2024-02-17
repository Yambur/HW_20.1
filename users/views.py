from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
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

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False

        send_mail(subject='Подтверждение адреса электронной почты',
                  message=f'Код для подтверждения {new_user.verify_code}',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[new_user.email],
                  )

        return redirect(reverse_lazy('users:verification'))


class ValidEmailView(View):
    template_name = 'users/verification.html'
    success_url = reverse_lazy('main:index')

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        verify_code = request.POST.get('verification')
        user = User.objects.filter(verify_code=verify_code).first()
        if user:
            user.is_verified = True
            user.save()
            return redirect('users:login')

        return redirect('users:verification')




    """def form_valid(self, form):
        user = User.objects.get()

        send_mail(
            subject='Регистрация на платформе',
            message=f"Код подтверждения: {user.verification}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email])
        return super().form_valid(form)"""

    #    if not user.email:
    #        token = secrets.token_urlsafe(16)
    #        user.activation_token = token
    #        user.save()

    #        send_mail(subject='Подтверждение адреса электронной почты',
    #                  message=f'Для подтверждения адреса электронной почты, копируйте данный пароль {token}',
    #                  from_email=settings.EMAIL_HOST_USER,
    #                  recipient_list=[user.email]
    #                  )

    #    return redirect(reverse_lazy('users:register'))
