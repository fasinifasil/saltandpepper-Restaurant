from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def IndexPage(request):
    return HttpResponse("Index page")
def PizzaPage(request):
    return HttpResponse('Pizza Page')