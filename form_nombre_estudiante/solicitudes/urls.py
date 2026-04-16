from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_solicitud, name='registrar_solicitud'),
    path('confirmacion/', views.confirmacion_solicitud, name='confirmacion_solicitud'),
]