# Control Gastos / Api-Rest con Django

[![Build Status](https://travis-ci.org/MatiasLoiseau/api-rest.svg?branch=master)](https://travis-ci.org/MatiasLoiseau/api-rest)
# Introducción

El objetivo de esta API será resolver el problema de llevar los movimientos monetarios diarios de una o más personas.
La API manejará los siguientes recursos:
* Cuentas
* Usuarios
* Movimientos
* Categorías de movimientos

El detalle sobre los recursos mencionados se encuentra [aquí](#recursos).

# Instalacion:
### Requisitos básicos
Deberá contar con los siguientes paquetes instalados:
* Python 2.7
* Django 1.11
* Django Rest Framework 3.7.3

En el apartado [Dependencias y Entorno Virtual](#dependencias-y-entorno-virtual) puede obtener más detalles sobre como crear un ambiente de aislado para su instalación utilizando virtualenv.

### Pasos para la instalación
A continuación se detallan los pasos para la instalación:

		git clone https://github.com/MatiasLoiseau/api-rest.git
		cd api-rest
		chmod a+x runserver.sh
		./runserver.sh


### Dependencias y Entorno Virtual
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

		# Distribuciones basadas en Debian:
		apt-get install httpie

		# Distribuciones basadas en RPM:
		yum install httpie

		# Arch Linux:
		pacman -S httpie
		
En caso de necesitar más información puede referirse a la [documentación](https://httpie.org/doc) de HTTPIE.

# Recursos

## Cuentas
#### Features
* Dar de alta una cuenta
* Listar todas las cuentas
* Listar una cuenta específica
* Modificar o borrar una cuenta

## Usuarios
#### Features
* Dar de alta un usuario
* Listar todas los usuarios
* Listar un usuario específico
* Modificar o borrar un usuario, eliminando también todos sus movimientos, en caso de contar con alguno

## Movimientos
#### Features
* Dar de alta un movimiento
* Listar todos los movimientos
* Listar un movimiento específico
* Modificar o borrar un movimiento

## Categorías de Movimientos
#### Features
* Dar de alta una categoría
* Listar todas las categorías
* Listar una categoría específica
* Modificar o borrar un categoría

# Test

-Para correr los test ejecutar:
```python manage.py test```
