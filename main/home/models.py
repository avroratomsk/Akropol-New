from django.db import models
from django.urls import reverse

from admin.singleton_model import SingletonModel

from django.core.exceptions import ValidationError



def validate_image_or_svg(value):
    import os
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".svg"]
    if ext not in valid_extensions:
        raise ValidationError("Неподдерживаемый формат. Разрешены: JPG, PNG, GIF, SVG.")

class BaseSettings(SingletonModel):
  logo  = models.ImageField(upload_to="base-settings", blank=True, null=True, verbose_name="Логотип")
  logo_footer = models.FileField(
     upload_to="base-settings",
     blank=True,
     null=True,
     verbose_name="Логотип Footer",
     validators=[validate_image_or_svg]
  )
  phone = models.CharField(max_length=50, blank=True, null=True, db_index=True, verbose_name="Номер телефона(Яковлева)")
  phone_two = models.CharField(max_length=50, blank=True, null=True, db_index=True, verbose_name="Номер телефона(Бедного)")
  time_work = models.CharField(max_length=250, blank=True, null=True, db_index=True, verbose_name="Время работы")
  time_work_two = models.CharField(max_length=250, blank=True, null=True, db_index=True, verbose_name="Время работы(выходные)")
  email = models.EmailField(max_length=250, blank=True, null=True, db_index=True, verbose_name="Email")
  address = models.CharField(max_length=250, blank=True, null=True, verbose_name="Адрес(Яковлева)")
  address_two = models.CharField(max_length=250, blank=True, null=True, verbose_name="Адрес(Бедного)")
  favicon = models.FileField(upload_to='base-settings/', blank=True, null=True, verbose_name="Favicon")
  

class HomeTemplate(SingletonModel):
  banner = models.ImageField(upload_to="home-page/", blank=True, null=True, verbose_name="Картинка главной страницы")
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  code_reviews = models.TextField(null=True, blank=True, verbose_name="Код отзывов")

class Contact(SingletonModel):
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  description = models.TextField(null=True, blank=True, verbose_name="Текст на страницу")
  code_map = models.TextField(null=True, blank=True, verbose_name="Код Яндекс карты")

class Stock(models.Model):
  """Model"""
  title = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название акции")
  description = models.TextField(blank=True, null=True, verbose_name="Описание акции")
  validity = models.DateTimeField(blank=True, null=True, help_text="После окончания акции, она перейдет в состояние не активна", verbose_name="Срок дейстия акции")
  status = models.BooleanField(default=True, verbose_name="Статус публикации")
  image = models.ImageField(upload_to="stock/", null=True, blank=True, verbose_name="ФОтография акции")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  slider_status = models.BooleanField(default=False, verbose_name="Слайдер на главной")

  def get_absolute_url(self):
      return reverse("stock_detail", kwargs={"slug": self.slug})
    
class GalleryCategory(models.Model):
  name = models.CharField(max_length=250, null=True, blank=True, verbose_name="Наименование")
  meta_h1 = models.CharField(max_length=350, null=True, blank=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="")
  home_view = models.BooleanField(default=False, verbose_name="Отображать на главной ?")
  image = models.ImageField(upload_to="gallery-category/", null=True, blank=True, verbose_name="Фотография категории")
  description = models.TextField(null=True, blank=True, verbose_name="Описание на странице")
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("gal_cat_detail", kwargs={"slug": self.slug})
  
class Gallery(models.Model):
  category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, null=True, default=None, related_name="categories")
  image = models.ImageField(upload_to="gallery-image/", null=True, blank=True, verbose_name="Фотография")
  name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Наименование пойдет в alt и title")
  cat_detail = models.BooleanField(default=False, verbose_name="Вывод в категорию")
  is_active = models.BooleanField(default=True, verbose_name="Выводить на сайт ?")
  work = models.BooleanField(default=False, verbose_name="Выводить на сайт ?")

  def __str__(self):
    return self.name
  
class RobotsTxt(models.Model):
  content = models.TextField(default="User-agent: *\nDisallow: /admin/")
    
  def __str__(self):
    return "robots.txt"


