from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #장고는 자체적으로 주소 마지막에 '/'를 붙이도록 설정되어있으므로 항상 '/'붙여주기!!
    #여기서는 프로젝틍 단위의 맴핑만 한다. 작은단위의 맵핑은 패로젝트 내에서 연결을 해준다.
    #그래서 include를 사용해서 해당 프로젝트로만 연결을 해주는 것이다.
    path('admin/', admin.site.urls),
    path('shoppingMall/', include('shoppingMall.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)