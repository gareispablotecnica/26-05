from django.urls import path
from .views import *

urlpatterns = [
    # ---> Pagina, Funcion , Hipervinculo
    path('',Home,name="Inicio"),
    path('registro/',Registro,name="Registro"),
    path('productos/',VerProductos,name="Productos"),

    path('Modificar/<ID_Alumno>/',Modificacion, name="Modificar"),
]
