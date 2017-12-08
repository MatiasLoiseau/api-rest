from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from cuenta.models import Cuenta
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from cuenta.serializer import CuentaSerializer


@csrf_exempt
#Lista o crea las cuentas
def cuenta_list(request):
    if request.method == 'GET':
        cuentas = Cuenta.objects.all()
        serializer = CuentaSerializer(cuentas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CuentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
#Modifica o borra
def cuenta_modify(request, pk):
    try:
        cuenta = Cuenta.objects.get(pk=pk)
    except Cuenta.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CuentaSerializer(cuenta)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CuentaSerializer(cuenta, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cuenta.delete()
        return HttpResponse(status=200)
