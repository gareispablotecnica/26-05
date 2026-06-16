from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *

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
    # --->Si el metodo de HTML es post
    if request.method=="POST":
        # --> Guarda lo que registro a la Base de DATOS
        query=FormularioRegistro(data=request.POST,files=request.FILES)
        if query.is_valid():
            query.save()
            data["Mensaje"]="Datos Registrados"
        else:
            data['Mensaje']="No se pudo Registrar"
    return render(request,'Pages/Registro.html',data)

def VerProductos(request):
    query=Alumnos.objects.all()
    data={
        'VerAlumnos':query
    }
    return render(request,'Pages/Alumnos.html',data)


def Modificacion(request,ID_Alumno):
    query=get_object_or_404(Alumnos, ID_Alumno=ID_Alumno)
    data={
        'Formulario':FormularioRegistro(instance=query)
    }
    # --->Si el metodo de HTML es post
    if request.method=="POST":
        # --> Guarda lo que registro a la Base de DATOS
        query=FormularioRegistro(data=request.POST,instance=query,files=request.FILES)
        if query.is_valid():
            query.save()
            data["Mensaje"]="Datos Modificados"
        else:
            data['Mensaje']="No se pudo Modificar"
    return render(request,'Pages/Registro.html',data)