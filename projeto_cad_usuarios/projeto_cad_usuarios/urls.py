

from django.urls import path
from app_cad_usuarios import views
urlpatterns = [
    #rota, view responsavel, nome de rerferencia
    path('',views.home,name='home'),
]