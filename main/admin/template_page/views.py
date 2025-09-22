from django.shortcuts import redirect, render
from home.models import HomeTemplate
from django.contrib import messages
from .forms import *

from .services.handle_admin_page import handle_admin_page

template_path = "common-template/page-template.html"

def admin_home_page(request):
  return handle_admin_page(
    request,
    model=HomeTemplate,
    form_class=HomeTemplateForm,
    title="Главная страница",
    template_path=template_path,
    extra_context={
      "meta_fields": ["meta_h1", "meta_title", "meta_description", "meta_keywords"],
      "right_fields": ["banner"],
    },
  )


def admin_settings(request):
  return handle_admin_page(
    request,
    model=BaseSettings,
    form_class=GlobalSettingsForm,
    title="Общие настройки сайта",
    template_path=template_path,
    extra_context={
      "left_fields": ["time_work", "time_work_two", "email"],
      "grid_fields": ["phone", "address", "phone_two", "address_two"],
      "right_fields": ["logo", "logo_footer", "favicon"],
    },
  )

def admin_contact(request):
  return handle_admin_page(
    request,
    model=Contact,
    form_class=ContactTemplateForm,
    title="Страница контактов",
    template_path=template_path,
    extra_context={
      "meta_fields": ["meta_h1", "meta_title", "meta_description", "meta_keywords"],
      "left_fields": ["description", "code_map"],
    },
  )


