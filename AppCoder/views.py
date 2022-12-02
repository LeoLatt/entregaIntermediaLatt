from django.shortcuts import render
from AppCoder.models import Negocio, Empleado, Producto
from AppCoder.forms import NegocioForm, EmpleadoForm, ProductoForm
from django.http import HttpResponse
#from django.template import Template, Context, loader



# Create your views here.
def inicio(request):
    
    return render (request, "inicio.html")


def negocio(request):

    negocio1=Negocio(nombre="HelthyFood",cuit=20111201302) #creo un objeto negocio
    
    negocio.save() #guardo la funcion

    cadena_Texto="Negocio guardado: "+negocio.nombre+" "+str(negocio.cuit)
    return HttpResponse(cadena_Texto)



def productos(request):
    return render (request, "productos.html")

def empleados(request):

    if request.method=="POST":
        form=EmpleadoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            cargo=informacion["cargo"]
            empleado= Empleado(nombre=nombre, apellido=apellido, email=email, cargo=cargo)
            empleado.save()
            return render (request, "inicio.html", {"mensaje": "EMPLEADO CREADO CORRECTAMENTE!!"})
    else:
        formulario=EmpleadoForm()
        return render (request, "empleados.html", {"form":formulario})


""" def pyFormulario(request):
    if request.method=="POST":
        nombrecito=request.POST["nombre"]
        comisioncita=request.POST["comision"]
        curso1=Curso(nombre=nombrecito,comision=comisioncita)
        curso1.save()
        return render (request, "AppCoder/inicio.html")
    return render(request, "AppCoder/cursoFormulario.html") """

def negocioFormulario(request):

    if request.method=="POST":
        form=NegocioForm(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            empresa=informacion["nombre"]
            numero=informacion["cuit"]

            negocio1=Negocio(nombre=empresa,cuit=numero)
            negocio1.save()
            return render (request, "inicio.html")
    else:
        formulario=NegocioForm()
        return render(request, "negocioFormulario.html", {"form":formulario})


def productoFormulario(request):

    if request.method=="POST":
        form=ProductoForm(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            categoria=informacion["categoria"]
            precio=informacion["precio"]
            vencimiento=informacion["vencimiento"]
            producto1=Producto(categoria=categoria,precio=precio,vencimiento=vencimiento)
            producto1.save()
            return render (request, "inicio.html", {"mensaje": "PRODUCTO CREADO CORRECTAMENTE"})
    else:
        formulario=ProductoForm()
        return render(request, "productoFormulario.html", {"form":formulario})



def busquedaNegocio(request):
    return render(request, "busquedaNegocio.html")

def negocios(request):
    return render (request, "negocios.html")


def buscar(request):

    if "cuit" in request.GET:

        cuit=request.GET["cuit"]

        negocios=Negocio.objects.filter(cuit__icontains=cuit)
        return render(request,"resultadosBusqueda.html", {"negocio":negocios} )
    else:
        return render(request, "busquedaNegocio.html", {"mensaje":"Ingrese un CUIT"})

#def listadenegocios(request):
  #  negocios=Negocio.objects.all()
   # return render(request, "Appcoder/listadenegocios.html", {"negocios":negocios})


def leerEmpleados(request):
    empleados=Empleado.objects.all()
    print(empleados)
    return render(request, "leerEmpleados.html", {"empleados":empleados})