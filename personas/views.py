from django.shortcuts import render
from .models import Persona
from .form import PersonaForm
# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)
def personaCreateView(request):
    print(request)
    if request.method == 'POST':
        nombre = request.POST.get('q')
        print(nombre)
    context = {}
    return render(request, 'personas/personascreate.html', context)


def searchForHelp(request):
    return render(request, 'personas/search.html', {})
def personasBuscarView(request):
    print('GET: ', request.GET)
    print('POST:', request.POST)
    context = {}
    return render(request, 'personas/personasBuscar.html', context)
