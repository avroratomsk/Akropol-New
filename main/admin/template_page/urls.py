from django.urls import path,include
from . import views



urlpatterns = [
  path('home-page/', views.admin_home_page, name='admin_home_page'),
  path('settings/', views.admin_settings, name='site_settings'),
  path('contact/', views.admin_contact, name='admin_contact'),
  path('ckeditor5/', include('django_ckeditor_5.urls')),
]