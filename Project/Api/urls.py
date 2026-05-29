from django.urls import path
from .views import *

urlpatterns = [
    # ---> Pagina, Funcion , Hipervinculo
    path('',Home,name="Inicio"),
]
