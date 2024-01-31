from django.urls import path

from main.apps import MainConfig
from main.views import IndexView, ContactsView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts')
]
