from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie	
from django.shortcuts import render

import json
from django.http import JsonResponse

from . import transaction
from evento.models import Evento

import requests

@csrf_exempt
def comprar(request):

	if request.method == 'POST':
		request.encoding = 'UTF-8'
		data = request.body.decode('UTF-8')
		json_data = json.loads(data)
		context = transaction.get_redirect_code(json_data)

	return JsonResponse(context)

@csrf_exempt
def notificacao(request):
    status=200

    if request.method == 'POST':
        request.encoding = 'ISO-8859-1'
        dataPost = dict((k, v) for k, v in request.POST.items())

        notification = transaction.get_notification(dataPost['notificationCode'])
        print(notification)

        try:
            codigo_pag_seguro = notification['transactionCode']
            status = notification['status']
            
            evento = Evento.objects.get(codigo_pag_seguro=codigo_pag_seguro)
            evento.status = status

            evento.save()
        except:
            print("Evento não encontrado")
            pass

    else:
        status=404

    return JsonResponse({'status':status})
