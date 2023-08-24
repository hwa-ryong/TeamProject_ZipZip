from django.urls import path
from . import views
app_name = 'calculate'

urlpatterns = [
    path('calculate/', views.calculate, name = 'calculate')
]