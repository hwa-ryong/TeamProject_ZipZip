from django.urls import path
from . import views

app_name = 'interior'

urlpatterns = [
    path('', views.board_interior, name='interior')
]