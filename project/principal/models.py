#encoding:utf-8 
from django.db import models 
from django.contrib.auth.models import User
#from google.appengine.ext import ndb

# Crear modelo 
class Noticia(models.Model):
    nombrenoticia = models.CharField(max_length=50, help_text='ingresa titulo')
    noticiaredac = models.TextField(max_length=100, help_text='redacta la noticia de futbol')
    imagen = models.ImageField(upload_to='fotos', verbose_name='Imagen')
    #Enlace al modelo Usuario que Django ya tiene construido
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombrenoticia

class Entrada(models.Model):
    #Dato cadena, longitud máxima 100 y único
    titulo = models.CharField(max_length=100, unique=True)
    #Dato texto, con texto de ayuda
    redac = models.TextField(help_text='Redacta antecedentes ')
    
    #Dato texto, con nombre: Preparación
    lugar = models.TextField(max_length =25,verbose_name='lugar del evento')
    
    #Dato imagen, se almacenarán en la carpeta recetas, titulo: Imágen
    imagen = models.ImageField(upload_to='fotos', verbose_name='Imagen')
    
    #Dato Fecha y Hora, almacena la fecha actual
    tiempo_registro = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    entradas = models.ForeignKey(Entrada)
    texto = models.TextField(help_text='Tu Comentario', verbose_name='Comentario')

    def __unicode__(self):
        return self.texto