from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from categoria.models import Categoria
from cuenta.models import Cuenta
from categoria.serializer import CategoriaSerializer


@csrf_exempt #eximo autentificacion
#Crea o lista a todas las categorias
def categoria_list(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt #eximo autentificacion
#Lista un categoria para una cuenta en particular (segun la pk enviada)
def categoria_get(request,pk):
    try:
        cuenta = Cuenta.objects.get(pk=pk)
    except categoria.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        categorias = Categoria.objects.filter(cuenta=cuenta.id)
        serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt #eximo autentificacion
#Te trae un categoria por su pk, lo modifica o borra
def categoria_modify(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(categoria,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        categoria.delete()
        return HttpResponse(status=410)