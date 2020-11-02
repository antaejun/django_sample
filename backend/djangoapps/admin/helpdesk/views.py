from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from backend.models import *


def helpdesk_list(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def helpdesk_detail(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def helpdesk_reply(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def helpdesk_reject(request):
  if request.method == 'GET':
      pass
  if request.method == 'POST':
      pass
  return JsonResponse({'result': 200})