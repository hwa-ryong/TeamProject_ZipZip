
from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'poll'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index_search, name='map_search'),
    path('index_search_list/', views.index_search_list, name='index_search_list'),
    path('test/', views.test_socal, name='test'),
    path('footer_source/', views.footer_source, name='footer_source'),
    path('footer_clause/', views.footer_clause, name='footer_clause'),
    path('footer_location/', views.footer_location, name='footer_location'),
    path('footer_personal/', views.footer_personal, name='footer_personal'),
]
