from django.shortcuts import render
# def ---> Funcion
# ---> Request : Retorna la Pagina Web
def Home(request):
    # -->Cada vez que llamemos a "Home"
    # --> estamos hablando de la pagina Base.html
    return render(request,'Base.html')