from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from backend.models import *


def deposit_info(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def deposit_request(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})

