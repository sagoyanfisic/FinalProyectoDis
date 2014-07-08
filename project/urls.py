
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from django.contrib.auth.views import login, logout, password_change 
#from qs.forms import ValidatingPasswordChangeForm


admin.autodiscover()

#if settings.DEBUG and settings.STATIC_ROOT:
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^$','principal.views.inicio'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^listaentrada/$','principal.views.lista_entrada'),
    url(r'^sobre/$','principal.views.sobre'),
    url(r'^noticia/$', 'principal.views.listanoticia'),
    url(r'^detentrada/(?P<id_receta>\d+)$','principal.views.detalle_entrada'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_URL,}
    ),

)
