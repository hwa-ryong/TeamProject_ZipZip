import urllib
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.forms import model_to_dict

from .models import SeouljRent, SeoulReal


# 지도 표시 html 보냄
def search(request):
    return render(request, 'map/search.html')

# 지도 검색 함수
def map_search(request):
    if request.method == 'GET':
        context = {}
        client_id = "Gr3DZKpSitjNw83linRK"
        client_secret = "CM1z5bCrQ6"
        query = request.GET.get('query')
        encText = urllib.parse.quote('{}'.format(query))
        sort = 'random'
        display = 5

        url = f"https://openapi.naver.com/v1/search/local.json?query={encText}&display={display}&sort={sort}"
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id", client_id)
        req.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(req)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            sub_items = []

            for item in items:
                sub_item = {
                    'title': item.get('title'),
                    'category': item.get('category'),
                    'address': item.get('address'),
                    'roadAddress': item.get('roadAddress')
                }
                sub_items.append(sub_item)
            context = {
                'items': sub_items,
            }
        else:
            print("Error Code:" + rescode)

        return JsonResponse(context)
    return JsonResponse({'result': '실패'})

# 데이터베이스 실거래가, 전월세가 파싱
def map_convert(request):
    if request.method == 'GET':
        seoul_rent = SeouljRent.objects.all()
        seoul_real = SeoulReal.objects.all()
        jrent = [model_to_dict(seoul) for seoul in seoul_rent]
        real = [model_to_dict(seoul) for seoul in seoul_real]

        results = {
            'jrent':jrent,
            'real':real
        }
        return JsonResponse(results, safe=False)

    return JsonResponse({'result': '실패'})