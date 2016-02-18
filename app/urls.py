#app/urls.py

from django.conf.urls import url
from django.conf.urls import patterns, include
from . import views
from app import views
from django.conf.urls import url, patterns, include

#from app.api import UsuarioResource

#usuario_resource=UsuarioResource()
#from .views import RegistrarUsuario, RedirigirUsuario



urlpatterns = [
    #url(r'^admin', views.libros, name='libros'),
    url(r'^$', views.index, name='index'),
    url(r'^app/$', views.index, name='base'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^login/$',views.login,name='login'),
    url(r'^registro/$',views.registro,name='registro'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^addbar/$',views.addbar,name='addbar'),
    url(r'^bar/(?P<category_name_slug>[\w\-]+)/$',views.bar,name='bar'),
    url(r'^bar/(?P<bar_name_url>[\w\-]+)/add_tapa/$', views.add_tapa, name='add_tapa'),
    url(r'^reclama_bares/$',views.reclama_bares,name='reclama_bares'),
    url(r'^reclama_visitas/$',views.reclama_visitas,name='reclama_visitas')
]