from django.shortcuts import render

# Create your views here.
def information(request):
    return render(request, 'information/information.html') # 알려드립니다메인

def info_budong(request):
    return render(request, 'information/category/info_budong.html')# 주택

def info_jutak(request):
    return render(request, 'information/category/info_jutak.html')# 주택

def info_trouble(request):
    return render(request, 'information/category/info_trouble.html')# 주택임대차분쟁

def info_gondong_trouble(request):
    return render(request, 'information/category/info_gondong_trouble.html') # 공동주택관리분쟁

def info_smart_blue(request):
    return render(request, 'information/smart/info_smart_blue.html') # 따라쟁이 청약

def info_smart_jansa(request):
    return render(request, 'information/smart/info_smart_jansa.html') # 따라쟁이 전세

def info_smart_mama(request):
    return render(request, 'information/smart/info_smart_mama.html') # 따라쟁이 매매