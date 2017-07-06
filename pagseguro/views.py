from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie	
from django.shortcuts import render

import json
from django.http import JsonResponse

from . import transaction

import requests

@csrf_exempt
def comprar(request):
    context = transaction.get_redirect_code()
    return JsonResponse(context)

@csrf_exempt
def notificacao(request):

    if request.method == 'POST':
        request.encoding = 'ISO-8859-1'
        dataPost = dict((k, v) for k, v in request.POST.items())

        notification = transaction.get_notification(dataPost['notificationCode'])
        print(notification)

    return render(request, 'notificacao/index.html', {})
