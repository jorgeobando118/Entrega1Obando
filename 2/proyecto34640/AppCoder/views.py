from django.shortcuts import render
from .models import Curso, Profesor, Estudiante
from django.http import HttpResponse

from django.urls import reverse_lazy

from AppCoder.forms import *

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
from django.shortcuts import render

def curso(request):

    curso1=Curso(nombre="Python",comision=34640)
    
    curso.save()
    cadena_Texto="Curso guardado: "+curso.nombre+" "+str(curso.comision)
    return HttpResponse(cadena_Texto)


def inicio(request):
    

    return render (request, "AppCoder/inicio.html")


def cursos(request):
    return render (request, "AppCoder/cursos.html")

def estudiantes(request):
    return render (request, "AppCoder/estudiantes.html")

def profesores(request):

    if request.method=="POST":
        form=ProfeForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            profesion=informacion["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "Appcoder/inicio.html", {"mensaje": "PROFESOR CREADO CORRECTAMENTE!!"})
    else:
        form=ProfeForm()


    return render (request, "AppCoder/profesores.html", {"form":form})

def ingresarProfesor(request):
    if request.method=="POST":
        form=ProfeForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            profesion=informacion["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "Appcoder/inicio.html", {"mensaje": "PROFESOR CREADO CORRECTAMENTE!!"})
    else:
        form=ProfeForm()


    return render (request, "AppCoder/ingresarProfesor.html", {"form":form})


def buscarProfesor(request):
    return render(request, "Appcoder/buscarProfesor.html")

def funcionbuscarProfesor(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        resultado=Profesor.objects.filter(nombre__icontains=nombre)
        return render(request,"Appcoder/resultadosBusquedaProfesor.html", {"Profesores":resultado} )
    else:
        return render(request, "Appcoder/resultadosBusquedaProfesor.html", {"mensaje":"No se encontro profesor"})





def ingresarEstudiante(request):
    if request.method=="POST":
        form=EstudianteForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            estudiante= Estudiante(nombre=nombre, apellido=apellido, email=email)
            estudiante.save()
            return render (request, "Appcoder/inicio.html", {"mensaje": "ESTUDIANTE CREADO CORRECTAMENTE!!"})
    else:
        form=EstudianteForm()


    return render (request, "AppCoder/ingresarEstudiante.html", {"form":form})                  


def buscarEstudiante(request):
    return render(request, "Appcoder/buscarEstudiante.html")

def funcionbuscarEstudiante(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        resultado=Estudiante.objects.filter(nombre__icontains=nombre)
        return render(request,"Appcoder/resultadosBusquedaEstudiante.html", {"Estudiantes":resultado} )
    else:
        return render(request, "Appcoder/resultadosBusquedaEstudiante.html", {"mensaje":"No se encontro estudiante"})


def ingresarCurso(request):
    if request.method=="POST":
        form=CursoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            comision=informacion["comision"]
            curso= Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, "Appcoder/inicio.html", {"mensaje": "CURSO CREADO CORRECTAMENTE!!"})
    else:
        form=CursoForm()

    return render (request, "AppCoder/ingresarCurso.html", {"form":form})  

def buscarCurso(request):
    return render(request, "Appcoder/buscarCurso.html")

def funcionbuscarCurso(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        resultado=Curso.objects.filter(nombre__icontains=nombre)
        return render(request,"Appcoder/resultadosBusquedaCurso.html", {"Cursos":resultado} )
    else:
        return render(request, "Appcoder/resultadosBusquedaCurso.html", {"mensaje":"No se encontro curso"})


def entregables(request):
    return render (request, "AppCoder/entregables.html")
"""
def cursoFormulario(request):

    if request.method=="POST":
        nombrecito=request.POST["nombre"]
        comisioncita=request.POST["comision"]

        curso1=Curso(nombre=nombrecito,comision=comisioncita)
        curso1.save()
        return render (request, "AppCoder/inicio.html")


    return render(request, "AppCoder/cursoFormulario.html") 

def cursoFormulario(request):

    if request.method=="POST":
        form=CursoForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombrecito=informacion["nombre"]
            comisioncita=informacion["comision"]

            curso1=Curso(nombre=nombrecito,comision=comisioncita)
            curso1.save()
            return render (request, "AppCoder/inicio.html")
    else:
        formulario=CursoForm()


    return render(request, "AppCoder/cursoFormulario.html", {"form":formulario})


def busquedaComision(request):
    return render(request, "Appcoder/busquedaComision.html")


def buscar(request):

    if request.GET["comision"]:

        comision=request.GET["comision"]

        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request,"Appcoder/resultadosBusqueda.html", {"cursos":cursos} )
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje":"CHE! Ingresa una comision"})




def leerProfesores(request):
    profesores=Profesor.objects.all()
    print(profesores)
    return render(request, "AppCoder/leerProfesores.html", {"profesores":profesores})


def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    profesor.delete()
    profesores=Profesor.objects.all()
    return render(request, "AppCoder/leerProfesores.html", {"mensaje":"Profesor eliminado correctamente", "profesores":profesores})

    
def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form=ProfeForm(request.POST)
        print(form)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
                  
            
            profesor.nombre=informacion["nombre"]
            profesor.apellido=informacion["apellido"]
            profesor.email=informacion["email"]
            profesor.profesion=informacion["profesion"]
            profesor.save()
            profesores=Profesor.objects.all()
            return render (request, "Appcoder/leerProfesores.html", {"mensaje": "PROFESOR EDITADO CORRECTAMENTE!!", "profesores":profesores})
    else:
        formulario= ProfeForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
    return render(request, "AppCoder/editarProfesor.html", {"form":formulario, "profesor":profesor})




#Vistas basadas en clases


class EstudianteList(ListView):
    model=Estudiante
    template_name="AppCoder/leerEstudiantes.html"

class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields=['nombre', 'apellido', 'email']

class EstudianteUpdate(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields=['nombre', 'apellido', 'email']

class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')

class EstudianteDetalle(DetailView):
    model=Estudiante
    template_name="Appcoder/estudiante_detalle.html"
"""
