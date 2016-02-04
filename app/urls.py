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
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^login/$',views.login,name='login'),
    url(r'^registro/$',views.registro,name='registro'),
]