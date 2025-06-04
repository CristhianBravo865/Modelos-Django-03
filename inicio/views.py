from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def myHomeView(request, *args, **kwargs):
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList': [],
    }
    return render(request, 'home.html', myContext) #Contexto
def anotherView(request):
    return HttpResponse("<h1>Solo otra pagina</h1>")