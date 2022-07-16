from django import forms

from .models import Sobre, Servicos
from django_svg_image_form_field import SvgAndImageFormField


class SobreForm(forms.ModelForm):
    class Meta:
        model = Sobre
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }

class ServicosForm(forms.ModelForm):
    class Meta:
        model = Servicos
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }