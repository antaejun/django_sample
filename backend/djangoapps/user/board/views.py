from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from backend.models import *
import json
from django.core.serializers import serialize


def board_list(request):
    type = request.GET.get('type','')
    sub_type = request.GET.get('sub_type','')   
    cur_page = request.GET.get('cur_page',1)
    start_num = (cur_page-1)*10
    page_size = 10
    count = 0
    board_list = ''

    if type == '': # Type이 존재하지않을 경우
        response = {
            'resultCode': 400,
            'resultMsg': 'no type parameter or type not exist'
        }
    else:
        if sub_type == '': # sub_type이 없는경우 해당 type 전체 조회
            count = TblBoard.objects.filter(type=type).count()
            board_list = TblBoard.objects.filter(type=type)[start_num:page_size]
        else: # sub_type이 있는경우 해당 type에 카테고리별 조회
            count = TblBoard.objects.filter(type=type,sub_type=sub_type).count()
            board_list = TblBoard.objects.filter(type=type,sub_type=sub_type)[start_num:page_size]

        board_list = json.loads(serialize('json', board_list))
        response = {
            'resultCode': 200,
            'resultMsg': 'success',
            'total_count': count,
            'cur_page': cur_page,
            'data': board_list
        }
    return JsonResponse(response)


def board_detail(request):
    id = request.GET.get('id',0)

    if id == 0:
        response = {
            'resultCode': 400,
            'resultMsg': 'id no parameter or id not exist'
        }
    board = TblBoard.objects.filter(id=id)
    board = json.loads(serialize('json', board))
    response = {
        'resultCode': 200,
        'resultMsg': 'success',
        'data': board
    }
    return JsonResponse(response)