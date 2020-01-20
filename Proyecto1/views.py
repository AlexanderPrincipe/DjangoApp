from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):

    p1 = Persona("Alexander", "Principe")

    fecha_actual = datetime.datetime.now()

    doc_externo = open("/home/alexander/Documentos/Proyectos/django/Proyecto1/Proyecto1/plantillas/index.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "fecha_actual": fecha_actual})

    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hello world")

def fechaactual(request):
    fecha = datetime.datetime.now()

    return HttpResponse(fecha)

def calculaEdad(request,edad, anio):

    #edadActual = 18
    periodo = anio-2019
    edadFutura = edad + periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(anio, edadFutura)

    return HttpResponse(documento)