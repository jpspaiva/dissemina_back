from django.contrib import admin

from .forms import SobreForm, ServicosForm

from .models import Inicio, Sobre, Servicos, Portfolio, Depoimentos, Contato, FormContato

class SobreFormAdmin(admin.ModelAdmin):
    form = SobreForm

class ServicoFormAdmin(admin.ModelAdmin):
    form = ServicosForm

# Register your models here.
class InicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    
admin.site.register(Inicio, InicioAdmin)
admin.site.register(Sobre, SobreFormAdmin)
admin.site.register(Servicos, ServicoFormAdmin)
admin.site.register(Portfolio)
admin.site.register(Depoimentos)
admin.site.register(Contato)

class FormContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(FormContato)