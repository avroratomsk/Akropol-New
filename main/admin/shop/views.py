from shop.models import *
from .forms import *
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import user_passes_test

general_url_product = "/admin/product/"

@user_passes_test(lambda u: u.is_superuser)
def admin_shop(request):
  try:
      shop_setup = ShopSettings.objects.get()
  except:
      shop_setup = ShopSettings()
      shop_setup.save()

  try:
      items = Product.objects.all()
  except:
      items = Product()

  if request.method == "POST":
    form_new = ShopSettingsForm(request.POST, request.FILES, instance=shop_setup)
    print(form_new)

    if form_new.is_valid:
      form_new.save()

      return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "shop/settings.html", {"form": form_new})
  form = ShopSettingsForm(instance=shop_setup)
  context = {
    "form": form,
    "items": items,
    "title": "Настройки магазина"
  }
  return render(request, "shop/settings.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product(request):
  """
  View, которая возвращаяет и отрисовывает все товары на странице
  и разбивает их на пагинацию
  """
  page = request.GET.get('page', 1)
  products = Product.objects.all()
  paginator = Paginator(products, 20)
  current_page = paginator.page(int(page))

  context = {
    "items": current_page
  }
  return render(request, "shop/product/product.html", context)

@user_passes_test(lambda u: u.is_superuser)
def product_edit(request, pk):
  """
    View, которая получает данные из формы редактирования товара
    и изменяет данные внесенные данные товара в базе данных
  """
  product = Product.objects.get(id=pk)
  product_image = ProductImage.objects.filter(parent=product)
  all_chars = Properties.objects.filter(parent=product)
  properties_form = ProductPropertiesForm()

  form = ProductForm(instance=product)

  form_new = ProductForm(request.POST, request.FILES, instance=product)

  if request.method == 'POST':
      if form_new.is_valid():
          form_new.save()
          product = Product.objects.get(id=pk)

          # Добавление новых характеристик
          prop_names = request.POST.getlist('new_name')
          prop_values = request.POST.getlist('new_value')

          for i in range(min(len(prop_names), len(prop_values))):
            Properties.objects.create(
                name=prop_names[i].strip(),
                value=prop_values[i].strip(),
                parent=product
            )

          # Обновление старых характеристик
          old_ids = request.POST.getlist('old_id')
          old_names = request.POST.getlist('old_name')
          old_values = request.POST.getlist('old_value')

          for i in range(min(len(old_ids), len(old_names), len(old_values))):
              prop = Properties.objects.get(id=old_ids[i])
              prop.name = old_names[i]
              prop.value = old_values[i]
              prop.save()


          images = request.FILES.getlist('src')

          for image in images:
              img = ProductImage(parent=product, src=image)
              img.save()

          return redirect(request.META.get('HTTP_REFERER'))
      else:
          return render(request, 'common-template/template-edit-add-page.html', {'form': form_new})
  context = {
    "form":form,
    "all_chars": all_chars,
    "title": "Страница редактирования",
    "url": general_url_product,
    "properties_form":properties_form,
    "product_image": product_image,
  }
  return render(request, "common-template/template-edit-add-page.html", context)

@user_passes_test(lambda u: u.is_superuser)
def product_add(request):
  form = ProductForm()

  if request.method == "POST":
    form_new = ProductForm(request.POST, request.FILES)
    if form_new.is_valid():
      form_new.save()
      return redirect('admin_product')
    else:
      return render(request, "common-template/template-edit-add-page.html", {"form": form_new})

  context = {
   "title": "Страница добавление",
   "url": general_url_product,
   "form": form
  }

  return render(request, 'common-template/template-edit-add-page.html', context)

def product_delete(request,pk):
  product = Product.objects.get(id=pk)
  product.delete()

  return redirect('admin_product')