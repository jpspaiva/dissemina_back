from django.contrib import admin

from .forms import DepoimentosForm, SobreForm, ServicosForm, PortfolioForm, InicioForm

from .models import Footer, Inicio, Sobre, Servicos, Portfolio, Depoimentos, Contato, FormContato


class SobreFormAdmin(admin.ModelAdmin):
    form = SobreForm


class ServicoFormAdmin(admin.ModelAdmin):
    form = ServicosForm


class PortfolioFormAdmin(admin.ModelAdmin):
    form = PortfolioForm


class DepoimentosFormAdmin(admin.ModelAdmin):
    form = DepoimentosForm


# Register your models here.


class InicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    form = InicioForm


admin.site.register(Inicio, InicioAdmin)
admin.site.register(Sobre, SobreFormAdmin)
admin.site.register(Servicos, ServicoFormAdmin)
admin.site.register(Portfolio, PortfolioFormAdmin)
admin.site.register(Depoimentos, DepoimentosFormAdmin)
admin.site.register(Contato)
admin.site.register(Footer)


class FormContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


admin.site.register(FormContato)
