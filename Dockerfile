FROM ubuntu:12.04

MAINTAINER Bogdan Alin Muresan <alinugr@gmail.com>

RUN apt-get update



#instalar dependencias
RUN apt-get install -y python-setuptools
RUN apt-get -y install python-dev
RUN apt-get -y install build-essential
RUN apt-get -y install python-psycopg2
RUN apt-get -y install libpq-dev
RUN easy_install pip
RUN pip install --upgrade pip

#Download the app
RUN apt-get install -y git
RUN git clone https://github.com/bogdananas/proyectoIV-modulo2.git

#instalamos la aplicaión
RUN cd proyectoIV-modulo2
RUN sudo pip install -r requirements.txt --allow-all-external