from django.urls import path

from . import views

app_name = 'notice'

urlpatterns = [
    path('notice/', views.notice, name='notice'),  # 자유게시판
    path('notice_view1/', views.notice_view1, name='notice_view1'), # 1번 게시판
    path('notice_view2/', views.notice_view2, name='notice_view2'), # 2번 게시판
    path('notice_view3/', views.notice_view3, name='notice_view3'), # 3번 게시판
    path('notice_view4/', views.notice_view4, name='notice_view4'), # 4번 게시판
    path('notice_view5/', views.notice_view5, name='notice_view5'), # 5번 게시판

]
