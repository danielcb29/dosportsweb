# dosportsweb
Proyecto DoSportsWeb para HackFoorGood 2016

#Integrantes
- Daniel Correa 
- Cristina Extremera
- Gerardo Bernal
- Alberto Ricci
- Daniel Rodríguez

#Instalación y requisitos
El proyecto esta realizando en Django 1.8.1 (Python3.*), Bootstrap3 y PostgreSQL 4.3

Los requisitos estan en requeriments.txt, para instalarlos se debe ejecutar
  
  `pip install -r requeriments.txt`
  
Se debe tener una base de datos de nombre dosports con usuario dosports y contraseña dosports 

#Ejecutar

Para ejecutar el proyecto una vez se tengan todos los requerimientos: 

  `python manage.py migrate`
  
  `python manage.py runserver` 
  
Ingresar a `http://localhost:8080` y ver el proyecto en vivo
