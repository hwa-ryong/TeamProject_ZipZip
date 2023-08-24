from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name="common/login.html"), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('mypage/', views.mypage, name='mypage'),
    path('<str:username>/', views.mypage_delete, name='mypage_delete'),
    path('mypage_update/<str:username>/', views.mypage_update, name='mypage_update'),
]