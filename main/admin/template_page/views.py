from django.shortcuts import redirect, render
from home.models import HomeTemplate
from django.contrib import messages
from .forms import *

template_path = "common-template/one-column-template.html"

def admin_home_page(request):
  settings, created = HomeTemplate.objects.get_or_create()  # либо достанет, либо создаст

  if request.method == "POST":
    form = HomeTemplateForm(request.POST, request.FILES, instance=settings)
    if form.is_valid():
      form.save()
      messages.success(request, "Изменения сохранены 🎉")
      return redirect(request.META.get('HTTP_REFERER', 'admin_home_page'))  # запасной redirect
    else:
      messages.error(request, "Исправьте ошибки в форме")
  else:
    form = HomeTemplateForm(instance=settings)

  context = {
    "form": form,
    "settings": settings,
    "title": "Главная страница"
  }
  return render(request, template_path, context)