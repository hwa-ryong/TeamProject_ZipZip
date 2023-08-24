import urllib
import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect

from map.models import SeouljRent, SeoulReal


def index(request):
    return render(request, 'poll/index.html')

def index2(request):
    return redirect('poll/')

def index_search(request):
    if request.method == 'GET':
        query = request.GET.get('search_data')

        context = {
            'query': query,
        }

        return JsonResponse(context)
    return render(request, 'poll/index.html')


def index_search_list(request):
    if request.method == 'GET':
        seoul_rent = SeouljRent.objects.all()
        seoul_real = SeoulReal.objects.all()
        jrent = [model_to_dict(seoul) for seoul in seoul_rent]
        real = [model_to_dict(seoul) for seoul in seoul_real]

        results = {
            'jrent': jrent,
            'real': real
        }
        return JsonResponse(results, safe=False)

    return redirect('poll/')

def test_socal(request):
    return render(request, 'poll/test.html')

def footer_source(request):
    return render(request, 'footer/출처.html')


def footer_clause(request):
    return render(request, 'footer/이용약관.html')


def footer_location(request):
    return render(request, 'footer/위치 기반 서비스.html')


def footer_personal(request):
    return render(request, 'footer/개인정보처리방침.html')