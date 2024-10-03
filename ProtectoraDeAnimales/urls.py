from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('animales', views.lista_animales, name='lista_animales'),
    path('colaboradores', views.lista_colaboradores, name='lista_colaboradores'),
    path('protectoras', views.lista_protectoras, name='lista_protectoras'),
]