from django.shortcuts import redirect, render
from django.contrib import messages
""" Данная функция создает функцию по шаблону """

def handle_admin_page(request, model, form_class, template_path, title, extra_context=None):
  settings, created = model.objects.get_or_create()

  if request.method == "POST":
    form = form_class(request.POST, request.FILES, instance=settings)
    if form.is_valid():
      form.save()
      messages.success(request, "Изменения сохранены 🎉")
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      messages.error(request, "Исправьте ошибки в форме")
  else:
    form = form_class(instance=settings)

  context = {
    "form": form,
    "settings": settings,
    "title": title,
  }

  if extra_context:
    for key, fields in extra_context.items():
      context[key] = [form[f] for f in fields]

  return render(request, template_path, context)
