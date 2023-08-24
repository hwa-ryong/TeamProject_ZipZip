from django.urls import path

from . import views

app_name = 'map'

urlpatterns = [
    path("", views.search, name="search"),   # 지도
    path("map_search/", views.map_search, name="map_search"),
    path("map_convert/", views.map_convert, name="map_convert"),
]
