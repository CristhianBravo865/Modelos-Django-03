from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def myHomeView(request, *args, **kwargs):
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList': [33, 44, 55],
    }
    return render(request, 'home.html', myContext) #Contexto
def anotherView(request):
    return HttpResponse("<h1>Solo otra pagina</h1>")

def filtros_template(request):
    return render(request, 'filtros.html', {
        'nombre': 'Cristhian',
        'lista': ['A', 'B', 'C'],
        'numero': 10,
        'fecha': datetime.now(),
        'vacia': ''
    })
