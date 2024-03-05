from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, ValidEmailView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reister/', RegisterView.as_view(), name='register'),
    path('verification/', ValidEmailView.as_view(), name='verification'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
]
