from django.contrib import admin
from django.urls import path, include
from chart import views                                     # !!!

urlpatterns = [
    path('', include('chart.urls')),
    path('world_population/',
         views.world_population, name='world_population'),  # 최상위 url 패턴에서 world 경로가 들어오면 view 로간다.
    path('admin/', admin.site.urls),
]