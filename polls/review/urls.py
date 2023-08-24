from django.urls import path

from . import views

app_name = 'review'

urlpatterns = [
    path('review_main/', views.review_list_main, name='review_main'), # 거래 후기 메인
    path('review_recommend/', views.review_recommend, name='review_recommend'),  # 거래후기 게시판 추천수 보기
    path('review_jan/', views.review_list_jan, name='review_jan'), # 거래후기전세
    path('review_jan_recommend/', views.review_list_jan_recommend, name='review_jan_recommend'), # 거래후기전세
    path('review_mama/', views.review_list_mama, name='review_mama'), # 거래후기매매
    path('review_mama_recommend/', views.review_list_mama_recommend, name='review_mama_recommend'), # 거래후기매매
    path('review_subscription/', views.review_list_subscription, name='review_subscription'), # 거래후기청약
    path('review_subscription_recommend/', views.review_list_subscription_recommend, name='review_subscription_recommend'), # 거래후기청약

    path('review_detail/<int:review_board_id>/', views.review_detail, name='review_detail'), # 거래후기보기

    path('review/<int:review_board_id>/', views.comment_create, name='comment_create'), # 댓글생성
    path('comment_update/<int:comment_id>',views.comment_update,name='comment_update'), # 댓글 수정
    path('comment_delete/<int:comment_id>',views.comment_delete,name='comment_delete'), # 댓글 삭제

    path('review_delete/<int:comment_id>',views.review_delete, name='review_delete'), # 게시판 삭제
    path('review_update/<int:review_board_id>',views.review_update, name='review_update'), # 게시판 수정

    path('review_wirte/', views.review_write, name='write'),


]
