import email
from django.shortcuts import render

from .models import Inicio, Sobre, Servicos, Portfolio, Depoimentos, Contato, FormContato

# Create your views here.


def index(request):

    inicio = Inicio.objects.last()
    sobre = Sobre.objects.first()
    servicos = Servicos.objects.all()[:3]
    portfolio = Portfolio.objects.all()[:4]
    depoimentos = Depoimentos.objects.all()[:3]
    contato = Contato.objects.last()
    formcontato = FormContato.objects.last()

    context = {
        'inicio': inicio,
        'sobre': sobre,
        'servicos': servicos,
        'portfolio': portfolio,
        'depoimentos': depoimentos,
        'contato': contato,
        'formcontato': formcontato
    }

    if request.method == 'POST':
        nome_form = request.POST['nome']
        telefone_form = request.POST['telefone']
        email_form = request.POST['email']
        texto_form = request.POST['mensagem']

        form = FormContato(nome=nome_form, telefone=telefone_form,
                           email=email_form, mensagem=texto_form)
        form.save()

    return render(request, 'index.html', context)
