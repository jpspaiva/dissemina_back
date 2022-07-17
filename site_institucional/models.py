from distutils.command.upload import upload
from django.db import models
from django.forms import CharField, EmailField, ImageField

# Create your models here.


class Inicio(models.Model):
    image = models.ImageField(verbose_name='Imagem Inicio', upload_to='fotos')
    titulo = models.CharField(verbose_name='Titulo Inicio', max_length=250)
    descricao = models.TextField(verbose_name='Descricao do Inicio')
    texto_button = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.titulo}'


class Sobre(models.Model):
    image = models.ImageField(verbose_name='Imagem Sobre', upload_to='sobre')
    titulo = models.CharField(verbose_name='Titulo Sobre', max_length=250)
    descricao = models.TextField(verbose_name='Descricao Sobre')

    def __str__(self):
        return f'{self.titulo}'


class Servicos(models.Model):
    image = models.ImageField(
        verbose_name='Imagem Servicos', upload_to='servicos')
    titulo = models.CharField(verbose_name='Titulo Servicos', max_length=250)
    subtitulo = models.CharField(
        verbose_name='Subtitulo Servicos', max_length=250)
    descricao = models.TextField(verbose_name='Descricao Servicos')

    def __str__(self):
        return f'{self.titulo}'


class Portfolio(models.Model):
    image = models.ImageField(
        verbose_name='Imagem Portifolio', upload_to='portifolio')
    titulo = models.CharField(verbose_name='Titulo Portifolio', max_length=250)
    subtitulo = models.CharField(
        verbose_name='Subtitulo Portifolio', max_length=250)
    descricao = models.TextField(verbose_name='Descricao Portifolio')

    def __str__(self):
        return f'{self.titulo}'


class Depoimentos(models.Model):
    image = models.ImageField(
        verbose_name='Imagem Depoimentos', upload_to='depoimentos')
    titulo = models.CharField(
        verbose_name='Titulo Depoimentos', max_length=250)
    cliente = models.CharField(verbose_name='Nome Cliente', max_length=250)
    ocupcliente = models.CharField(
        verbose_name='Ocupacao Cliente', max_length=20)
    depoimento = models.TextField(verbose_name='Depoimento')

    def __str__(self):
        return f'{self.cliente}'


class Contato(models.Model):
    email = models.EmailField()
    telefone = models.CharField(verbose_name='Telefone', max_length=12)
    endereco = models.CharField(verbose_name='Endereco', max_length=100)

    def __str__(self):
        return f'{self.email}'


class FormContato(models.Model):
    nome = models.CharField(verbose_name='Nome Form', max_length=20)
    telefone = models.CharField(verbose_name='Telefone Form', max_length=12)
    email = models.EmailField(verbose_name='Email Form')
    mensagem = models.TextField(verbose_name='Mensagem Form', max_length=400)
    textbutton = models.CharField(verbose_name='Texto Button', max_length=20)

    def __str__(self):
        return f'{self.nome}'


class Footer(models.Model):
    instagram = models.CharField(max_length=15)
    facebook = models.CharField(max_length=15)
    youtube = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.instagram}'
