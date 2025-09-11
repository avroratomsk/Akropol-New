from django import forms
from home.models import HomeTemplate
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