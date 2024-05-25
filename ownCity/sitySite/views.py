from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Главная</h2>")

def news(request):
    return HttpResponse("<h2>Новости города</h2>")

def goverment(request):
    return HttpResponse("<h2>Руководство города</h2>")

def facts(request):
    return HttpResponse("<h2>Факты о городе</h2>")

def contacts(request):
    return HttpResponse("<h2>Контактные телефоны городских служб</h2>")
