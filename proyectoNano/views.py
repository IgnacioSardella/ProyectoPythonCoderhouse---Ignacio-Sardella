from django.http import HttpResponse
from django.template import Context, Template, loader
from aplication.models import *
from random import randint

def Bienvenida(request):
    return HttpResponse("Messi te amo")

def bienvenidaTemplate(request):
    name = "Nano"
    edad = 20
    notas = [2, 7, 10, 10, 8, 6]
    
    dict = {"nombre" : name, "edad": edad, "notas": notas}
    
    plantilla = loader.get_template('bienvenido.html')    
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def agregar_curso(request):
    nro_comision = randint(1, 99999)
    str_nombre = "Python"
    curso = Curso(nombre=str_nombre, comision=nro_comision)
    curso.save()
    doc = f'<html><h1>se creo el curso {str_nombre} para la comision {nro_comision}</h1></html>'
    return HttpResponse(doc)