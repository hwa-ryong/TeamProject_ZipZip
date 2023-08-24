from django.urls import path
from . import views

app_name = 'introduction'

urlpatterns = [
    path('introduction/', views.introduction , name='introduction')
]
