from django.urls import path

from main.apps import MainConfig
from main.views import IndexView, ContactsView, BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, \
    BlogDeleteView, toggle_activity, ProductCreateView, ProductListView, ProductUpdateView, CategoryListView, \
    ProductDetailView, CategoryDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('products/<int:pk>/', ProductListView.as_view(), name='product_list'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),

    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),

    path('blog/activity/<int:pk>', toggle_activity, name='toggle_activity'),
]
