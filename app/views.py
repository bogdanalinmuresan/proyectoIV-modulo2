# -*- coding: utf-8 -*-
import hashlib
from django.shortcuts import render
#from app.models import Libro
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
import mongoengine 
from mongoengine.context_managers import switch_collection
from app.models import Usuario,Tapas,Bares
from models import Usuario
from django.contrib.auth.models import User
from django.http import JsonResponse

#from forms import UsuarioForm



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

    return render(request, 'index.html', context_dict)


def bar (request,category_name_slug):
    context_dict={}
    bar=Bares.objects.get(nombre=category_name_slug)
    print "entra en .view.bar"
    context_dict['category_name']=bar.nombre
    context_dict['category']=bar#aumentamos el nr de visitas al bar

   

    if request.method=='POST':
        nom_tapa=request.POST.get('id_tapa')
        if nom_tapa!='':
            tapa=Tapas(nombre=nom_tapa,nrvotos='1')
            print "nom_tapa",nom_tapa

            tapa.save()
            print "nombre de la tapa", tapa.nombre
            #añadimos la tapa al bar
            bar.tapas=[tapa]
            
            bar.save()
            for b in bar.tapas:
                print b.nombre
    
    return render(request,'bar.html',context_dict)


def about(request):
    return render(request,'about.html')

def add_tapa(request,bar_name_url):
    context_dict={}
    bar=Bares.objects.get(nombre=bar_name_url)
    print "entra en add_tapa"
    context_dict['category_name']=bar.nombre
    context_dict['category']=bar

    print "numero de visitas antes de incrementar" ,bar.nrvisitas
    var=bar.nrvisitas
    var=var+1
    bar.nrvisitas=var
    print "numero de visitas despues de incrementar" ,bar.nrvisitas
    bar.save()

    if request.method=='POST':
        nom_tapa=request.POST.get('id_tapa')
        if nom_tapa!='':
            tapa=Tapas(nombre=nom_tapa,nrvotos='1')
            print "nom_tapa",nom_tapa

            tapa.save()
            print "nombre de la tapa", tapa.nombre
            #añadimos la tapa al bar
            bar.tapas.append(tapa)
            bar.save()
            for b in bar.tapas:
                print b.nombre
    return render(request,'bar.html',context_dict)

def logout(request):

    del request.session['email']
    del request.session['authenticated']
    del request.session['username']
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        
        password=request.POST.get('id_password')
        email=request.POST.get('id_email')

        usuario=Usuario.objects(email=email)

        #obtener hash la contraseña y compararla, si coinciden
        m = hashlib.md5()
        m.update(password)
        hashPass=m.hexdigest()
        
        #print user._query
        #print user.explain()
        if hashPass==usuario.password:
            #print hashPass
            #print usuario.password
            login=True
            request.session['email']=usuario.email
            request.session['username']=usuario.username
            request.session['authenticated']=True
            return render(request,'index.html',{'login':login,'user':usuario,})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def registro(request):
    if request.method=='POST':
        username=request.POST.get('id_username')
        email=request.POST.get('id_email')
        password1=request.POST.get('id_password1')
        password2=request.POST.get('id_password2')

        print "username=",username
        print "email=",email
        print "password1=",password1
        print "password2=",password2


        #user_form=UsuarioForm(data=request.POST)
        #if user_form.is_valid():
        print "formulario correcto"

        #comprobar que las contraseñas coinciden
        if password1==password2:
            print "contraseñas coinciden"
            #comprobar que el email del usuario no existe en la base de datos
            userBD=Usuario.objects(email=email)
            #print userBD.email
            #aplicacion de hash sobre el password 
            m = hashlib.md5()
            m.update(password1)
            hashPass=m.hexdigest()
            
            #no existe ese usuario
            if userBD.count()==0:
                print "user es none"
                user=Usuario(username=username,email=email,password=hashPass)
                #user.switch_collection('usuarios')
                user.save()
                res='<div class="alert alert-warning alert-dismissable"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>Usuario existente!</strong> Ya hay un usuario registrado con este correo .</div>'
                return render(request,'index,html',{'registrado':res})
            
            else:
                print "existe el ususario en la base de datos",userBD
                res='<div class="alert alert-warning alert-dismissable"> <button type="button" class="close" data-dismiss="alert">&times;</button> <strong>Gracias por registrarse</strong> Acaba usted de registrarse ,puede iniciar sesión.</div>'
                return render(request,'registro.html',{'registrado':res})

    return render(request,'registro.html')


def addbar(request):
    if request.method=='POST':
        print "entra en view"
        nombre_bar=request.POST.get('id_bar')
        direc_bar=request.POST.get('id_direccion')

        bar=Bares(nombre=nombre_bar,direccion=direc_bar,nrvisitas=0)
        bar.save()
    
        print bar.nombre
        print bar.direccion
    return render(request,'add_bar.html')

def reclama_bares(request):
    misbares=Bares.objects.all()

    lista_bares=[]

    for b in misbares:
        lista_bares.append(b.nombre)

    return JsonResponse(lista_bares,safe=False)


def reclama_visitas(request): 
    misbares=Bares.objects.all()

    lista_visitas=[]

    for b in misbares:
        lista_visitas.append(b.nrvisitas)

    return JsonResponse(lista_visitas,safe=False)