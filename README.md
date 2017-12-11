# Control Gastos / Api-Rest con Django

[![Build Status](https://travis-ci.org/MatiasLoiseau/api-rest.svg?branch=master)](https://travis-ci.org/MatiasLoiseau/api-rest)
# Tabla de Contenidos

1. [Introducción](#introducción)
2. [Instalación](#instalación)
	* [Requisitos básicos](#requisitos-básicos)
	* [Pasos para la instalación](#pasos-para-la-instalación)
	* [Dependencias y Entorno Virtual](#dependencias-y-entorno-virtual)
	* [HTTPIE](#httpie)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Recursos](#recursos)
	* [Cuentas](#cuentas)
	* [Usuarios](#usuarios)
	* [Movimientos](#movimientos)
	* [Categorías](#categorías)
5. [Test](#test)

---

# Introducción

El objetivo de esta API será resolver el problema de llevar los movimientos monetarios diarios de una o más personas.
La API manejará los siguientes recursos:
* [Cuentas](#cuentas)
* [Usuarios](#usuarios)
* [Movimientos](#movimientos)
* [Categorías](#categorías)

Todos los pedidos son devueltos en formato JSON.

Para ver el apartado completo sobre los recursos mencionados haga click [aquí](#recursos).

---

# Instalación:
### Requisitos básicos
Deberá contar con los siguientes paquetes instalados:
* Python 3.5
* Django 1.11
* Django Rest Framework 3.7.3

En el apartado [Dependencias y Entorno Virtual](#dependencias-y-entorno-virtual) puede obtener más detalles sobre como crear un ambiente de aislado para su instalación utilizando virtualenv.
___
### Pasos para la instalación
A continuación se detallan los pasos para la instalación:

		git clone https://github.com/MatiasLoiseau/api-rest.git
		cd api-rest
		chmod a+x runserver.sh
		./runserver.sh

___
### Dependencias y Entorno Virtual
El entorno virtual ya cuenta con los paquetes necesarios para poder utilizar la API.
Para activarlo ejecutar lo siguiente:
	
		virtualenv /env
		source env/bin/activate
		
En caso de que no sea posible su instalación o se indique que aún faltan dependencias.
Puede proceder a generar su propio entorno virtual, siguiendo estos pasos:

		virtualenv env
		source env/bin/activate
		pip3 install django
		pip3 install djangorestframework

___
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

---

# Estructura del proyecto

### Archivos del proyecto
Se listarán los archivos principales del proyecto, con el fin de explicar su propósito:
* manage.py: Se crea automáticamente en cada proyecto de Django manage.py, contempla tareas administrativas.
* settings.py: Este archivo contiene todas las configuraciones para el proyecto, apps instaladas, paths de recursos utilizados, entre otros.
* urls.py: Contiene las rutas (URLs) que están disponibles en el proyecto.
___
### Archivos de los recursos
Se listarán los archivos principales de los recursos, con el fin de explicar su propósito:
* serializer.py: Los serializers permiten que datos complejos, como los conjuntos de consultas y las instancias del modelo, se conviertan en tipos de datos nativos de Python que luego se pueden representar fácilmente en formatos como JSON.
* models.py: Contiene los campos y comportamientos esenciales de los recursos.
* views.py: Contiene la lógica que será utilizada para devolver los responses en función de los request realizados.
* tests.py: Contiene los tests correspondientes a cada recurso.
___
### Modelado de los datos
Se ha utilizado el ORM (Object-Relational Mapping) provisto por Django.

Por lo tanto, una vez creados los modelos de datos (archivo *models.py*), Django proporcionó automáticamente una abstracción que permitió crear, recuperar, actualizar y eliminar objetos. 

La base de datos utilizada para guardar los datos generados fue _sqlite_, la cuál se incluye por default en la instalación de Django.

[Este documento](https://docs.djangoproject.com/en/2.0/topics/db/queries/) explica con más detalle como utilizar el ORM de Django.

----

# Recursos

## Cuentas
Podrán pertenecer a más de un usuario, deben contener un nombre.
___
### Atributos
##### * id:
	Integer. Valor autoincremental que se generará automáticamente.
##### * nombre:
	String. Denominación de la cuenta. 
___	
### Métodos
#### Dar de alta una cuenta
##### Parámetros
* id
* nombre
##### Request
	 http POST  http://{$PATH}/controlgastos/cuentas/ nombre="nombre_de_cuenta"
##### Responses
Algunas de las posibles respuestas:
* 201: La cuenta ha sido generada correctamente
* 400: En caso de que el request este mal escrito, o que falte el campo de nombre
* 500: Error en el servidor

#### Listar las cuentas
##### Parámetros
* id -> solo en caso de querer ver los detalles de una cuenta específica, en caso contrario no se deberá pasar ningún parámetro
##### Request
Listar todas las cuentas

	http GET http://{$PATH}/controlgastos/cuentas/
	
Ver los detalles de una cuenta

	http GET http://{$PATH}/controlgastos/cuentas/{$id}
	
Listar todos los usuarios de una cuenta

	http GET http://{$PATH}/controlgastos/cuentas/{$id (cuenta)}/usuarios/
	
Listar todas las categorías de una cuenta

	http GET http://{$PATH}/controlgastos/cuentas/{$id (cuenta)}/categorias/

##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor

Si la respuesta es exitosa se devolverá el recurso en formato JSON
Ejemplo:

		HTTP/1.1 200 OK
		Content-Length: 39
		Content-Type: application/json
		Date: Sat, 06 Dec 2017 22:41:16 GMT
		Server: WSGIServer/0.2 CPython/3.5.3
		X-Frame-Options: SAMEORIGIN

		[
		    {
			"id": 1, 
			"nombre": "cuenta_ejemplo"
		    }
		]

#### Modificar una cuenta
##### Parámetros
* id -> Primary Key de la Cuenta
* Atributos que se desee modificar. [(Ver Atributos de la Cuenta)](#cuentas)
##### Request
	http PUT http://{$PATH}/controlgastos/cuentas/{$id}/  nombre="nuevo_nombre_de_cuenta"
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor

En caso de que la respuesta sea exitosa, también será devuelto el recurso modificado en formato JSON
Ejemplo:

		HTTP/1.1 200 OK
		Content-Length: 45
		Content-Type: application/json
		Date: Sat, 06 Dec 2017 23:01:18 GMT
		Server: WSGIServer/0.2 CPython/3.5.3
		X-Frame-Options: SAMEORIGIN

		{
		    "id": 1, 
		    "nombre": "nuevo_nombre_de_cuenta"
		}

#### Borrar una cuenta
##### Parámetros
* id -> Primary Key de la Cuenta
##### Request
	http DELETE http://{$PATH}/controlgastos/cuentas/{$id}/  
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor

***

## Usuarios
Todos usuarios deben tener una cuenta asociada,los atributos correspondientes al recurso se listan a continuación.

### Atibutos
##### * id:
	Integer. Valor autoincremental que se generará automáticamente.
##### * user:
	String. Nombre del usuario. 
##### * password:
	String. Contraseña del usuario.
##### * email:
	String. E-mail del usuario.
##### * cuenta:
	Cuenta del usuario, clave foránea. Correspondiente a la pk (id) de una cuenta previamente generada.
___

### Métodos
#### Dar de alta un usuario
##### Parámetros
* id
* user
* password
* e-mail
* cuenta
##### Request
	  http POST http://localhost/controlgastos/usuarios/ user="user_ejemplo_1" email=usrejemplo@ejemplo.com cuenta=<id de cuenta> password="ejemplo"

##### Responses
Algunas de las posibles respuestas:
* 201: La cuenta ha sido generada correctamente
* 400: Puede ser Bad Request si: 1° Tipo de dato incorrecto, 2° Falta un campo, 3° No encuentra el ID de la cuenta
* 500: Error en el servidor

#### Listar los usuarios
##### Parámetros
* id -> solo en caso de querer ver los detalles de un usuario específico, en caso contrario no se deberá pasar ningún parámetro
##### Request
	http GET http://{$PATH}/controlgastos/usuarios/{$id}
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor

Si la respuesta es exitosa se devolverá el recurso en formato JSON
Ejemplo:

		HTTP/1.1 201 Created
		Content-Length: 101
		Content-Type: application/json
		Date: Sun, 10 Dec 2017 00:37:11 GMT
		Server: WSGIServer/0.2 CPython/3.5.3
		X-Frame-Options: SAMEORIGIN

		{
		    "cuenta": 2, 
		    "email": "ejemplo@ejemplo.com", 
		    "id": 3, 
		    "password": "ejemplo", 
		    "user": "ejemplo_user"
		}

#### Modificar un usuario
##### Parámetros
* id -> Primary Key del Usuario
* Atributos que se desee modificar. [(Ver Atributos del Usuario)](#usuarios)
##### Request
	http PUT http://{$PATH}/controlgastos/usuarios/{$id}/  atributo="nuevo_valor"
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el usuario que se desea modificar
* 500: Error en el servidor

En caso de que la respuesta sea exitosa, también será devuelto el recurso modificado en formato JSON
Ejemplo:

		HTTP/1.1 200 OK
		Content-Length: 112
		Content-Type: application/json
		Date: Sun, 10 Dec 2017 00:43:59 GMT
		Server: WSGIServer/0.2 CPython/3.5.3
		X-Frame-Options: SAMEORIGIN

		{
		    "cuenta": 2, 
		    "email": "ejemplo@ejemplo.com", 
		    "id": 3, 
		    "password": "ejemplo", 
		    "user": "ejemplo_user_modificado"
		}

#### Borrar un usuario
##### Parámetros
* id -> Primary Key del Usuario
##### Request
	http DELETE http://{$PATH}/controlgastos/usuarios/{$id}/  
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor

***
## Categorías

### Atributos
##### * id:
	Integer. Valor autoincremental que se generará automáticamente.
##### * nombre:
	String. Denominación de la categoría.
##### * cuenta:
	Cuenta a la cual corresponde la categoría. Clave foránea (id) de una cuenta previamente generada.
	
#### Métodos
#### Dar de alta una categoría
##### Parámetros
* id
* nombre
* cuenta
##### Request
	 http POST http://localhost:8000/controlgastos/categorias/ nombre=cat1 cuenta=2
##### Responses
Algunas de las posibles respuestas:
* 201: La cuenta ha sido generada correctamente
* 400: Puede ser Bad Request si: 1° Tipo de dato incorrecto, 2° Falta un campo, 3° No encuentra el ID de la cuenta
* 500: Error en el servidor

#### Listar las categoría
##### Parámetros
* id -> solo en caso de querer ver los detalles de una cuenta específica, en caso contrario no se deberá pasar ningún parámetro
##### Request
	http GET http://{$PATH}/controlgastos/categorias/{$id}
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor

Si la respuesta es exitosa se devolverá el recurso en formato JSON
Ejemplo:

		HTTP/1.1 200 OK
		Content-Length: 40
		Content-Type: application/json
		Date: Sun, 10 Dec 2017 01:52:40 GMT
		Server: WSGIServer/0.2 CPython/3.5.3
		X-Frame-Options: SAMEORIGIN

		{
		    "cuenta": 2, 
		    "id": 1, 
		    "nombre": "cat1"
		}
		
#### Modificar una categoria
##### Parámetros
* id -> Primary Key de la Categoria
* Atributos que se desee modificar. [(Ver Atributos de la Categoria)](#categorias)
##### Request
	http PUT http://{$PATH}/controlgastos/cateogorias/{$id}/  nombre="nuevo_nombre_de_categoria"
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor

En caso de que la respuesta sea exitosa, también será devuelto el recurso modificado en formato JSON
Ejemplo:

		HTTP/1.1 200 OK
		Content-Length: 51
		Content-Type: application/json
		Date: Sun, 10 Dec 2017 02:15:45 GMT
		Server: WSGIServer/0.2 CPython/3.5.3
		X-Frame-Options: SAMEORIGIN

		{
		    "cuenta": 2, 
		    "id": 1, 
		    "nombre": "cate_modificada"
		}

#### Borrar una categoria
##### Parámetros
* id -> Primary Key de la Categoría
##### Request
	http DELETE http://{$PATH}/controlgastos/categorias/{$id}/  
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor
***

## Movimientos
### Atibutos
##### * id
 	Integer. Valor autoincremental que se generará automáticamente.	
##### * fecha:
	Date. Fecha en la cual se registró el movimiento. 
##### * user:
	Usuario que ha generado el movimiento.Correspondiente a la clave foránea (id) de un usuario previamente generado.
##### * monto:
	Float. Importe del movimiento generado.
##### * categoria:
	Categoría del movimiento. Correspondiente a la clave foránea (id) de una categoría previamente generada.
##### * descripcion:
	(Campo opcional) Descripción del movimiento, el valor indicado por default es "operación de compra-venta".
	
### Métodos
#### Dar de alta un movimiento
##### Parámetros
* user
* monto
* categoría
* descripción (opcional)
##### Request
	  http POST http://localhost/controlgastos/movimientos/ user="1" monto="10" categoria=1 descripcion="alquileres"
##### Responses
Algunas de las posibles respuestas:
* 201: La cuenta ha sido generada correctamente
* 400: Puede ser Bad Request si: 1° Tipo de dato incorrecto, 2° Falta un campo, 3° No encuentra el ID del usuario o categoria
* 500: Error en el servidor

#### Listar los movimientos
##### Parámetros
* id -> solo en caso de querer ver los detalles de un movimiento específico, en caso contrario no se deberá pasar ningún parámetro
##### Request
Listar todos los movimientos

	http GET http://{$PATH}/controlgastos/movimientos/
	
Ver detalles de un movimiento

	http GET http://{$PATH}/controlgastos/movimientos/{$id}
	
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor

Si la respuesta es exitosa se devolverá el recurso en formato JSON
Ejemplo:

		HTTP/1.1 200 OK
		Content-Length: 130
		Content-Type: application/json
		Date: Sun, 10 Dec 2017 02:25:17 GMT
		Server: WSGIServer/0.2 CPython/3.5.3
		X-Frame-Options: SAMEORIGIN

		[
		    {
			"categoria": 1, 
			"descripcion": "operacion compra-venta", 
			"fecha": "2017-12-10T02:13:05.896", 
			"id": 1, 
			"monto": "10", 
			"user": 3
		    }
		]

#### Modificar un movimiento
##### Parámetros
* id -> Primary Key del Movimiento
* Atributos que se desee modificar. [(Ver Atributos del Movimiento)](#movimientos)
##### Request
	http PUT http://{$PATH}/controlgastos/movimientos/{$id}/  atributo="nuevo_valor"
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el usuario que se desea modificar
* 500: Error en el servidor

En caso de que la respuesta sea exitosa, también será devuelto el recurso modificado en formato JSON
Ejemplo:

		HTTP/1.1 200 OK
		Content-Length: 133
		Content-Type: application/json
		Date: Sun, 10 Dec 2017 02:26:12 GMT
		Server: WSGIServer/0.2 CPython/3.5.3
		X-Frame-Options: SAMEORIGIN

		{
		    "categoria": 1, 
		    "descripcion": "operacion compra-venta", 
		    "fecha": "2017-12-10T02:13:05.896", 
		    "id": 1, 
		    "monto": "1000000", 
		    "user": 3
		}

#### Borrar un movimiento
##### Parámetros
* id -> Primary Key del Movimiento
##### Request
	http DELETE http://{$PATH}/controlgastos/movimientos/{$id}/  
##### Responses
Algunas de las posibles respuestas:
* 200: En caso de que la consulta haya sido realizada con éxito
* 404: En caso de que no haya sido encontrado el objeto
* 500: Error en el servidor

***

# Test

### Fixtures
Han sido utilizados para completar automáticamente datos y que nos mismos no contengan errores que no permitan que el test continúe.
##### Generación
	python3 manage.py dumpdata > path/to/app/fixtures/data.json
##### Carga
	from django.core.management import call_command
	call_command('loaddata', 'data.json', app_label='aplicacion')

### Ejecución de los test
Para correr los test los pasos son los siguientes:
En caso de que se quiera correr algun cambio se podrá generar la migración.

		python3 manage.py makemigrations
		python3 manage.py migrate
		python3 manage.py test
		
Para testear solo un recurso en particular:

		python3 manage.py test <nombre recurso>.tests
