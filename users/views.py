from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

import secrets
from users.forms import RegisterUserForm, UserForm
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
        new_user.save()

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
        verify_code = request.POST.get('code')
        user = User.objects.filter(verify_code=verify_code).first()
        if user:
            user.is_verified = True
            user.is_active = True
            user.save()
            return redirect('users:login')
        else:
            return redirect('main:index')


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

def generate_new_password(request):
    user = request.user
    new_pass = User.objects.make_random_password()
    user.set_password(new_pass)
    user.save()

    send_mail(
        subject='Поздравляем с изменением пароля',
        message='Ваш новый пароль: {}'.format(new_pass),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )

    return redirect(reverse('users:login'))
