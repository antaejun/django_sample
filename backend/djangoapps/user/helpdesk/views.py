from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from backend.models import *
from django.core.serializers import serialize
from .forms import HelpdeskForm
import json
import datetime


def helpdesk_list(request):
    user_id = request.GET.get('user_id',0)
    type = request.GET.get('type','')
    sub_type = request.GET.get('sub_type','')

    if user_id == 0: # 파라미터에 id가 존재하지않거나 해당id DB에 존재하지않을경우
        response = {
            'resultCode': 400,
            'resultMsg': 'no user_id parameter or user_id not exist'
        }
    else:
        if (type == '' and sub_type == '') or type == '': # 전체 조회
            helpdesk_list = TblHelpdesk.objects.filter(user_id=user_id)
        elif sub_type == '': # type별 조회
            helpdesk_list = TblHelpdesk.objects.filter(user_id=user_id,type=type)
        else: # 카테고리별 조회
            helpdesk_list = TblHelpdesk.objects.filter(user_id=user_id,type=type,sub_type=sub_type)

        helpdesk_list = json.loads(serialize('json', helpdesk_list))
        response = {
            'resultCode': 200,
            'resultMsg': 'success',
            'data': helpdesk_list
        }    
    return JsonResponse(response)


def helpdesk_detail(request):
    id = request.GET.get('id',0)

    if id == 0:
        response = {
            'resultCode': 400,
            'resultMsg': 'no id parameter or id not exist'
        }
    else:
        helpdesk = TblHelpdesk.objects.filter(id=id)

        helpdesk = json.loads(serialize('json',helpdesk))
        response = {
            'resultCode': 200,
                'resultMsg': 'success',
                'data': helpdesk
        }
    return JsonResponse(response)

@csrf_exempt
def helpdesk_write(request):
    print(request.POST)
    form = HelpdeskForm(request.POST)
    now = datetime.datetime.now()
    if form.is_valid():
        tbl_helpdesk = TblHelpdesk()
        tbl_helpdesk.type = form.cleaned_data['type']
        tbl_helpdesk.sub_type = form.cleaned_data['sub_type']
        tbl_helpdesk.title = form.cleaned_data['title']
        tbl_helpdesk.content = form.cleaned_data['content']
        tbl_helpdesk.user_id = form.cleaned_data['user_id']
        tbl_helpdesk.status = 'N'
        tbl_helpdesk.delete_yn = 'N'
        tbl_helpdesk.created_at = now.strftime('%Y-%m-%d %H:%M:%S')

        tbl_helpdesk.save()
        response = {
            'resultCode': 200,
            'resultMsg': 'success'
        }  
    else:
        response = {
            'resultCode': 400,
            'resultMsg': 'valid error'
        }  
        
    return JsonResponse(response)