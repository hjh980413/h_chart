from django.contrib import admin
from django.urls import path
from chart import views                                     # !!!

urlpatterns = [
    path('', views.home, name='home'),  # home 을 보여줌
    path('ticket-class/1/',  # class1 을 보여줌
         views.ticket_class_view_1, name='ticket_class_view_1'),
    path('ticket-class/2/',  # class2 을 보여줌
         views.ticket_class_view_2, name='ticket_class_view_2'),
    path('ticket-class/3/',  # class3 을 보여줌
         views.ticket_class_view_3, name='ticket_class_view_3'),
    path('covid/', views.covid, name='covid'),
    path('world-population/',
         views.world_population, name='world_population'),  # !!!
    path('json-example/', views.json_example, name='json_example'),
    path('json-example/data/', views.chart_data, name='chart_data'),

    path('admin/', admin.site.urls),
]