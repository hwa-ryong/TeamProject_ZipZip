from django.urls import path

from . import views

app_name = 'koreaCalendar'

urlpatterns = [
    path('', views.koreaCalendar, name='subCalendar'),  # 달력
    path('koreaCalendar/calendar_iframe/<str:title>/', views.koreaCalendar_iframe, name='subCalendar_iframe'),
]
