from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_asistencia, name='registrar_asistencia'),
    path('confirmacion/', views.confirmacion_asistencia, name='confirmacion_asistencia'),
]