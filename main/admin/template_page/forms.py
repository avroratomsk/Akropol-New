from django import forms
from home.models import *
from ..widgets import *
from django_ckeditor_5.widgets import CKEditor5Widget

from admin.forms import INPUT_CLASS

class HomeTemplateForm(forms.ModelForm):
  """ Form, редактирование главной страницы"""

  class Meta:
      model = HomeTemplate
      fields = "__all__"
      widgets = {
          'name': forms.TextInput(attrs={
              'class': INPUT_CLASS
          }),
          'meta_h1': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'meta_title': forms.TextInput(attrs={
              'class': f"{INPUT_CLASS} meta_title",
          }),
          'meta_description': forms.Textarea(attrs={
              'class': f"{INPUT_CLASS} meta_description",
              'rows': 5
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
      }


class GlobalSettingsForm(forms.ModelForm):
  """ Form, глобальные и общие настройки сайта(лого, телефон, email)"""

  class Meta:
    model = BaseSettings
    fields = "__all__"

    widgets = {
      'phone_two': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'phone': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'time_work': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'time_work_two': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'email': forms.EmailInput(attrs={
        'class': INPUT_CLASS
      }),
      'address': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'address_two': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'meta_title': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'meta_description': forms.TextInput(attrs={
         'class': f"{INPUT_CLASS} meta_description",
         'rows': 5
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
#       'description':CKEditor5Widget(
#         attrs={'class': 'django_ckeditor_5'},
#         config_name='extends'
#       )
    }

class ContactTemplateForm(forms.ModelForm):
  """ Форма страницы контакты """

  class Meta:
    model = Contact
    fields = "__all__"

    widgets = {
      'meta_h1': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'meta_title': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'meta_description': forms.TextInput(attrs={
         'class': f"{INPUT_CLASS} meta_description",
         'rows': 5
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'code_map': forms.TextInput(attrs={
        'class': f"{INPUT_CLASS} meta_description",
        'rows': 5
      }),
#       'description':CKEditor5Widget(
#         attrs={'class': 'django_ckeditor_5'},
#         config_name='extends'
#       )
    }
