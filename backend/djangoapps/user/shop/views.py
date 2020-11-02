from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from backend.models import *
import json
from django.core.serializers import serialize
from collections import defaultdict

def shop_list(request):
    cur_page = request.GET.get('cur_page',1)
    start_num = (int(cur_page)-1)*10
    page_size = 10

    with connections['default'].cursor() as cur:
        query = '''
            select R1.* 
            from (
			    select p.id,
				   p.product_name,
                   p.product_desc,
                   p.product_price,
				   ROW_NUMBER() OVER (PARTITION BY id ORDER BY id) as RN,
                   f.enc_file_name,
                   f.file_ext,
                   f.save_path
			    from tbl_product p 
			    left join tbl_file f 
			    on p.id = f.type_id 
		        )R1
            WHERE R1.RN =1 limit {start_num},{page_size}
        '''.format(start_num=start_num,page_size=page_size)
        cur.execute(query)
        rows = cur.fetchall()
        print(list(rows))
        rowsData = list(rows)
        resultList = []
    try:
        
        for item in rowsData:
            id = item[0]       
            product_name = item[1]
            product_desc = item[2]
            product_price = item[3]
            enc_file_name = item[5]
            file_ext = item[6]
            save_path = item[7]
            resultData = {
                "product_name":product_name,
                "product_desc":product_desc,
                "product_price":product_price,
                "enc_file_name":enc_file_name,
                "file_ext":file_ext,
                "save_path":save_path
            }
           
            #resultList.append(json.dumps(jsonData))
            resultList.append(resultData)
            print(resultList)
            print(type(resultList[0]))
            
        result_code = 200
    except BaseException as err:
        resultData = {
            "product_name":'',
            "product_desc":'',
            "product_price":0,
            "enc_file_name":'',
            "file_ext":'',
            "save_path":''
        }
        resultList.append(resultData)
        #resultList.append(json.dumps(jsonData))
        result_code = 400

    response = {
        'resultCode': result_code,
        'resultMsg': 'success',
        'resultData': resultList
    }
    return JsonResponse(response)
  

def shop_detail(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_buy(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_add_cart(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_cart_list(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})


def shop_history_list(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    return JsonResponse({'result': 200})