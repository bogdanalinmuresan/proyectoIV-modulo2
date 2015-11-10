
# -*- coding: utf-8 -*-

from django.shortcuts import render
#from app.models import Libro
from django.http import HttpResponse
from django.views import generic



def libros(request):
	#La parte lógica
	#lista_libros = Libro.objects.order_by('­fecha')[:10]
	return render(request, 'libros.html')

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "are you am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'hello.html', context_dict)