from django.urls import path
from . import views

app_name = 'information'

urlpatterns = [
    path('information/', views.information, name='information'),
    path('info_budong/', views.info_budong, name='info_budong'),
    path('info_jutak/', views.info_jutak, name='info_jutak'),
    path('info_trouble/', views.info_trouble, name='info_trouble'),
    path('info_gondong_trouble/', views.info_gondong_trouble, name='info_gondong_trouble'),
    path('info_smart_blue', views.info_smart_blue, name='info_smart_blue'),
    path('info_smart_jansa', views.info_smart_jansa, name='info_smart_jansa'),
    path('info_smart_mama', views.info_smart_mama, name='info_smart_mama'),
]
