from django import forms

from .models import Inicio, Sobre, Servicos, Portfolio, Depoimentos
from django_svg_image_form_field import SvgAndImageFormField

class InicioForm(forms.ModelForm):
    class Meta:
        model = Inicio
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }

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


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }


class DepoimentosForm(forms.ModelForm):
    class Meta:
        model = Depoimentos
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }
