	# Create your views here.
from principal.models import Noticia, Entrada, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage


def sobre(request):
	html = "<html><body>Proyecto de lala</body></html>"
	return HttpResponse(html)
def listanoticia(request):
	noticia = Noticia.objects.all()
	return render_to_response('listanoticias.html',{'lista':noticia}, context_instance = RequestContext(request))
def inicio(request):
	entrada = Entrada.objects.all()
	return render_to_response('inicio.html',{'entrada':entrada}, context_instance = RequestContext(request))
def usuarios(request):
	usuarios = User.objects.all()
	entrada = Entrada.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios, 'entrada':entrada})
def lista_entrada(request):
	entrada = Entrada.objects.all()
	return render_to_response('recetas.html', {'datos':entrada}, context_instance = RequestContext(request))
def detalle_entrada(request, id_entrada):
	dato = get_object_or_404(Entrada, pk = id_entrada)
	comentarios = Comentario.objects.filter(entrada = dato)
	return render_to_response('receta.html', {'entrada':dato, 'comentarios':comentarios}, context_instance = RequestContext(request))
	