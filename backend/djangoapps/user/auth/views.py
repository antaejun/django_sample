from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from backend.models import TblUsers
from backend.djangoapps.common.decorators import login_check, allow_post, allow_get, allow_user, allow_admin


@csrf_exempt
@allow_post
def signin(request):
    account = request.POST.get('account')
    password = request.POST.get('password')

    user = TblUsers.objects.filter(account=account, password=password)

    if len(user) != 0: # 로그인 처리
        user = user.first()
        request.session['id'] = user.id
        request.session['is_staff'] = user.is_staff
        response = {
            'resultCode': 200,
            'resultMsg': 'success'
        }    
    else: # 정보 일치하지 않을 경우
        response = {
            'resultCode': 400,
            'resultMsg': 'account or password do not match'
        }
    return JsonResponse(response)
    


def signup(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def find_id(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def find_pw(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def user_detail(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def change_password(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


@csrf_exempt
@allow_get
@login_check
@allow_user
def my_point(request):
    id = request.session['id']

    # 반드시 데이터가 없을 경우에 대해 예외처리가 필요함
    try:
        user = TblUsers.objects.get(id=id)
        point = user.point
        recycle_point = user.recycle_point
        jnc_point = user.jnc_point
        result_code = 200
    except BaseException as err:
        point = 0
        recycle_point = 0
        jnc_point = 0
        result_code = 400

    response = {
        'resultCode': result_code,
        'resultMsg': 'success',
        'resultData': {
            'point': point,
            'recycle_point': recycle_point,
            'jnc_point': jnc_point
        }
    }
    return JsonResponse(response)
    


