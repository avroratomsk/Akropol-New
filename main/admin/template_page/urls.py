from django.urls import path
from . import views



urlpatterns = [
  path('home-page/', views.admin_home_page, name='admin_home_page'),
]