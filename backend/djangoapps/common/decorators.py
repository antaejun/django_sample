from django.http import HttpResponse, JsonResponse


# 로그인 여부 체크
def login_check(func):
    def wrapper(request, *args, **kwargs):
        if 'id' in request.session:
            pass
        else:
            response = {
                'resultCode': 401,
                'resultMsg': 'You are not login'
            }
            return JsonResponse(response)
        result = func(request, *args, **kwargs)
        return result
    return wrapper


# 사용자 여부 체크
def allow_user(func):
    def wrapper(request, *args, **kwargs):
        if 'is_staff' in request.session:
            if request.session['is_staff'] == 0:
                pass
            else:
                response = {
                    'resultCode': 403,
                    'resultMsg': 'Administrator is not allowed'
                }
                return JsonResponse(response)
        else:
            response = {
                'resultCode': 400,
                'resultMsg': 'Bad Request'
            }
            return JsonResponse(response)
        result = func(request, *args, **kwargs)
        return result
    return wrapper


# 관리자 여부 체크
def allow_admin(func):
    def wrapper(request, *args, **kwargs):
        if 'is_staff' in request.session:
            if request.session['is_staff'] == 1:
                pass
            else:
                response = {
                    'resultCode': 403,
                    'resultMsg': 'General User is not allowed'
                }
                return JsonResponse(response)
        else:
            response = {
                'resultCode': 400,
                'resultMsg': 'Bad Request'
            }
            return JsonResponse(response)
        result = func(request, *args, **kwargs)
        return result
    return wrapper


# GET 메소드 여부 체크
def allow_get(func):
    def wrapper(request, *args, **kwargs):
        if request.method == 'GET':
            pass
        else:
            response = {
                'resultCode': 405,
                'resultMsg': 'Do not allow it other than GET method'
            }
            return JsonResponse(response)
        result = func(request, *args, **kwargs)
        return result
    return wrapper


# POST 메소드 여부 체크
def allow_post(func):
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            pass
        else:
            response = {
                'resultCode': 405,
                'resultMsg': 'Do not allow it other than POST method'
            }
            return JsonResponse(response)
        result = func(request, *args, **kwargs)
        return result
    return wrapper


