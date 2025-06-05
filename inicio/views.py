from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def myHomeView(request, *args, **kwargs):
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList': [33, 44, 55],
    }
    return render(request, 'home.html', myContext) #Contexto
def anotherView(request):
    return HttpResponse("<h1>Solo otra pagina</h1>")
def prueba_if_basico(request):
    return render(request, 'prueba_if_basico.html', {'numero': 40})
