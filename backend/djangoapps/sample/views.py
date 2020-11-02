from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from backend.models import *


# pep 규정 상 문법은 모두 '_' 표기법으로 작성할 것
# camel 표기법 사용 금지
# 함수 띄어쓰기는 2칸 스페이스
# 탭은 4칸 기준으로 작성


# json 반환 하는 방법
def sample_default(request):
    return JsonResponse({'result': 200})


# raw 쿼리 기반 controller
# sql injection 공격에 취약함
# raw query 기반이기 때문에 러닝커브가 없음
# 소스 가독성이 저하됨
def sample_raw_query(request):
    account = '93immm'

    with connections['default'].cursor() as cur:
        query = '''
            select point, recycle_point, jnc_point
            from tbl_users
            where account='{account}';
        '''.format(account=account)
        cur.execute(query)
        rows = cur.fetchall()

    # 반드시 데이터가 없을 경우에 대해 예외처리가 필요함
    try:
        user = rows[0]
        point = user[0]
        recycle_point = user[1]
        jnc_point = user[2]
        result_code = 200
    except BaseException as err:
        point = 0
        recycle_point = 0
        result_code = 0
        resultCode = 400

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


# ORM 쿼리 기반 controller
# sql injection 공격이 통하지 않음
# ORM을 학습하는데 시간이 걸림
# 소스 가독성이 향상됨
def sample_orm(request):
    account = '93immm'

    # 반드시 데이터가 없을 경우에 대해 예외처리가 필요함
    try:
        user = TblUsers.objects.get(account=account)
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