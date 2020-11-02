from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from backend.models import *


def index(request):
    context = {}
    return render(request, 'dev/index.html', context)
