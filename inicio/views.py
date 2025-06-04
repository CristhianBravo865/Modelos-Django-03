from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def myHomeView(request):
    return render(request, 'home.html', {})
def anotherView(request):
    return HttpResponse("<h1>Solo otra pagina</h1>")