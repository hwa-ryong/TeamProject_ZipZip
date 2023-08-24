"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poll/', include('poll.urls')),
    path('', views.index2),
    path('community/', include('community.urls')),
    path('notice/', include('notice.urls')),
    path('information/', include('information.urls')),
    path('news/', include('news.urls')),
    path('interior/', include('interior.urls')),
    path('review/', include('review.urls')),
    path('introduction/', include('introduction.urls')),
    path('calculate/', include('calculate.urls')),
    path('map/', include('map.urls')),
    path('koreaCalendar/', include('koreaCalendar.urls')),
    path('common/', include('common.urls')),
    path('accounts/', include('allauth.urls')),
]
