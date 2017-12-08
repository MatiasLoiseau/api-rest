from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from usuario.models import Usuario
from cuenta.models import Cuenta
from movimiento.models import Movimiento
from movimiento.serializer import MovimientoSerializer


@csrf_exempt #eximo autentificacion
#Crea o lista a todos los movimiento
def movimiento_list(request):
    if request.method == 'GET':
        movimientos = Movimiento.objects.all()
        serializer = MovimientoSerializer(movimientos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovimientoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt #eximo autentificacion
#Lista un movimiento para una categoria en particular (segun la pk enviada)
def movimiento_get(request,pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Movimiento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        movimientos = Movimiento.objects.filter(categoria=categoria.id)
        serializer = MovimientoSerializer(movimientos, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt #eximo autentificacion
#Te trae un movimiento por su pk, lo modifica o borra
def movimiento_modify(request, pk):
    try:
        movimiento = Movimiento.objects.get(pk=pk)
    except Movimiento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MovimientoSerializer(movimiento)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovimientoSerializer(movimiento,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        movimiento.delete()
        return HttpResponse(status=200)
