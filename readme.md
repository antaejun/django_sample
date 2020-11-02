### 개발환경
```
cmder
python 3.6.8

모듈 관련 정보는 requirements.txt 참고
```

### 개발환경구축
```
windows 기반 설명

cd ~
mkdir workspace
cd workspace
https://github.com/h4ppyy/jij-backend
cd jij-backend
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

### visual studio code 연동 참고
https://code.visualstudio.com/docs/python/tutorial-django

### response 공통 스펙
```
response = {
	'resultCode': 200,
	'resultMsg': 'success',
	'resultData': None,
}
```

### response resultCode 정의
```
200 - 성공
400 - 일반적인 오류 전부
401 - 로그인 하지 않은 상태
403 - 허용되지 않은 권한
405 - 허용되지 않은 메소드
```

### 데코레이션 순서 
```
데코레이션은 반드시 위에서 아래로 실행됨
따라서 아래의 순서를 지켜줘야함

1. @csrf_exempt
2. @allow_get or @allow_post
3. @login_check
4. @allow_user or @allow_admin
```