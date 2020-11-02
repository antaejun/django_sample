from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from backend.models import *


def shop_list(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_detail(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_create(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_update(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_display(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_option_display(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_history(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def cart_list(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})