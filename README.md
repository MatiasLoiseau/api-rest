# Control Gastos / Api-Rest con Django

[![Build Status](https://travis-ci.org/MatiasLoiseau/api-rest.svg?branch=master)](https://travis-ci.org/MatiasLoiseau/api-rest)
# Introducción
El objetivo de esta API será resolver el problema de llevar los movimientos monetarios diarios de una o más personas.
La API manejará los siguientes recursos:
* Cuentas
* Usuarios
* Movimientos
* Categorías de movimientos
[acac](#recursos)

# Instalacion:

		git clone https://github.com/MatiasLoiseau/api-rest.git
		cd api-rest
		chmod a+x runserver.sh
		./runserver.sh


### Virtualenv
El entorno virtual ya cuenta con los paquetes necesarios para poder utilizar la API.
Para activarlo ejecutar lo siguiente:
	
		virtualenv /env
		source env/bin/activate
		
En caso de que no sea posible su instalación o se indique que aún faltan dependencias.
Puede proceder a generar su propio entorno virtual, siguiendo estos pasos:

		virtualenv env
		source env/bin/activate
		pip install django
		pip install djangorestframework



### HTTPIE
Las consultas de prueba sobre la API fueron realizadas con HTTPIE, se pueden encontrar ejemplos en el archivo [SET PRUEBA](https://github.com/MatiasLoiseau/api-rest/blob/master/SET%20PRUEBA)

Para su instalación deberán realizarse los siguientes pasos:

# Recursos
## Usuarios
## Cuentas
## Movimientos
## Categorías de Movimientos
## Test

-Para correr los test ejecutar:
```python manage.py test```
