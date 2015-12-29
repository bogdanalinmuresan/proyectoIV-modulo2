## **Proyecto de infraestructura virtual junto con desarrollo de aplicaciones para Internet** ##

[![Build Status](https://travis-ci.org/bogdananas/proyectoIV-modulo2.svg?branch=master)](https://travis-ci.org/bogdananas/proyectoIV-modulo2)

**Estamos inscritos en el certamen de proyectos de la UGR organizado por la OSL.**

## **Hito 1: Merka** ##

### **Participantes:** ###

### Ángel Valera Motos  ###
### Bogdan Alin Muresan ###

**Descripción:**

Nuestra aplicación se trata de un sistema de gestión de paquetes, de modo que la aplicación web será una tienda online, desarrollada en python, en un framework de alto nivel como Django. Dicha tienda consistirá en que tu puedes comprar algún tipo de producto, realizar un seguimiento de dicho producto.

El proyecto se va a desarrollar en dos módulos, dentro de un repositorio principal de  tipo [organización](https://github.com/ProyectoIV-DAI/ProyectoIV-Modulo-Principal.git):

**El módulo 1:**  [(Ángel Valera Motos )](https://github.com/AngelValera/proyectoIV-Modulo-1.git)Este módulo se encarga de toda la gestión de las bases de datos necesarias. Al tratarse de una tienda online necesitaremos base de datos (MySQL) replicadas, una base de datos para usuarios, para productos, etc. 

**El módulo 2:** [(Bogdan Alin Muresan )](https://github.com/bogdananas/proyectoIV-modulo2.git) Este módulo se encarga del alojamiento web de la aplicación, en el servidor así como la conexión de la aplicación con las bases de datos y el despliegue de la misma.

Hemos elegido llevar a cabo este proyecto, porque se centra en la virtualización de recursos como puede ser el uso de máquinas virtuales para el despliegue de una aplicación para Internet, usando también para ello un framework de alto nivel.

##Infraestructura
Mi proyecto se va a desplegar en [heroku](https://www.heroku.com/) ([mas info](https://github.com/bogdananas/proyectoIV-modulo2/blob/master/docs/heroku.md)) y consiste en un  blog donde los usuarios realizan comentarios. Se podrá permitir crear y consultar los comentarios realizados por etiquetas.

Darse de alta el la plataforma ,asi como iniciar sesión.

La base de datos usada es mongodb y se aloja en un servidor ofrecido por [mongolab](https://mongolab.com/) 


El lenguaje utilizado es python y como framework utilizaremos Django.
 


##	Integración Continua:Travis
Vamos a elegir un sistema de integración continua como travis para que cuando se realize una modificación en nuestro repositorio ,se compruebe que se han pasado los tests.

Creación del archivo [.travis.yml](https://github.com/bogdananas/proyectoIV-modulo2/blob/master/.travis.yml)


Configuramos el repositorio

![configuracion repo](http://i1175.photobucket.com/albums/r624/Bob_Mures/travis_repo_zpsfwsw9dis.png)




##Despliegue en un Paas:Heroku

Elegimos Heroku como PaaS porque es el PaaS que mejor se adapta a nuestras necesidades , y es sencillo de usar.

La aplicación funcionando [http://damp-sea-7668.herokuapp.com/app](http://damp-sea-7668.herokuapp.com/app)


[Mas info](https://github.com/bogdananas/proyectoIV-modulo2/blob/master/docs/heroku.md)

##Crear la base de datos:mongolab

Nos damos de alta en mongolab y creamos una base de datos.
Para la conexión a la base de datos utilizamos Pymongo

![http://i1175.photobucket.com/albums/r624/Bob_Mures/mongolab_zpsbz0cnt8t.png](http://i1175.photobucket.com/albums/r624/Bob_Mures/mongolab_zpsbz0cnt8t.png)



