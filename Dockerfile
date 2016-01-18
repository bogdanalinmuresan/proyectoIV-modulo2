FROM UBUNTU:12.04

MAINTAINER Bogdan Alin Muresan <alinugr@gmail.com>

#-y ejecutar sin preguntar
RUN sudo apt-get -y update

#Download the app
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/bogdananas/proyectoIV-modulo2.git

#instalar dependencias
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

#instalamos la aplicaión
RUN cd proyectoIV-modulo2
RUN pip install -r requirements.txt --allow-all-external