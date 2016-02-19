##	Desplieque en un PaaS : [Heroku](https://www.heroku.com/) 

Descargamos e Instalamos el **toolbelt de heroku** en nuestra máquina 

    pip install django-toolbelt
    
 En nuestro proyecto Django creamos el archivo **Procfile** con eso estamos indicando que usamos el servidor WSGI gunicorn.
    
    web: gunicorn miprojecto.wsgi —log-file
    
Especificamos las dependencias de nuestro proyecto ,en el fichero,necesario para el despliegue en heroku

 **requierements.txt**

~~~
Django==1.8
django-tastypie==0.12.2
djangorestframework==3.3.1
gunicorn==19.4.1
mongoengine==0.10.5
pymongo==3.2
python-dateutil==2.4.2
python-mimeparse==0.1.4
six==1.10.0
wheel==0.24.0
whitenoise==2.0.6
~~~


Los pasos de comandos para conseguir el despliegue ha sido el siguiente
 
~~~
install django-toolbelt
heroku login
heroku create
git add .
git commit -m "despliegue automático en heroku"
git push heroku master
heroku ps:scale web=1
heroku open app
~~~

La aplicación se encuentra desplegada en :[http://damp-sea-7668.herokuapp.com/app](http://damp-sea-7668.herokuapp.com/app)

