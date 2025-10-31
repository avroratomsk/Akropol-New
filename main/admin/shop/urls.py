from django.urls import path, include

from . import views

urlpatterns = [
    #URl - отвечающие за отображение товаров, редактирование и удаление товара
    path('admin-shop/', views.admin_shop, name='admin_shop'),
    path('product/', views.admin_product, name='admin_product'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
]