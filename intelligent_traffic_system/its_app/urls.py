from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulate/', views.run_simulation, name='simulate'),
    path('get_logs/', views.get_logs, name='get_logs'),
]