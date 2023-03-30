#confing/urls.py에서는 프로젝트 단위의 맵피만해주기 위해 프로제거트 내부에 urls.py파일을 따로 만들어서 config/urls.py와 연결을 해준다.

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('main/', views.mainPage, name='mainPage'),
    # <<<  !!TEST!!  >>>
    path('', views.home),
    path('upload/', views.upload_imgae, name='upload'),
    path('result/', views.check),
] 

