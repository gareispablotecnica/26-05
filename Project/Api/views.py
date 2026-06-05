from django.shortcuts import render
from .forms import *

# def ---> Funcion
# ---> Request : Retorna la Pagina Web
def Home(request):
    # -->Cada vez que llamemos a "Home"
    # --> estamos hablando de la pagina Base.html
    return render(request,'Base.html')

def Registro(request):
    data={
        'Formulario':FormularioRegistro()
    }
    return render(request,'Pages/Registro.html',data)