from django.conf.urls import url
from django.conf.urls import patterns, include
from . import views
from app import views


#from .views import RegistrarUsuario, RedirigirUsuario



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^libros/$', views.libros, name='libros'),
]