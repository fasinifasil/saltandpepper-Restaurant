from django.http import HttpResponse
from django.shortcuts import render

from BaseApp.models import PizzaModel, BurgerModel


# Create your views here.
def IndexPage(request):
    context={'active_link':'index'}
    return render(request,'food/index.html',context)
def PizzaPage(request):
    pizzas=PizzaModel.objects.all()
    context =   {'item':pizzas,'active_link':'pizzas'}
    return render(request,'food/pizza.html',context)
def BurgerPage(request):
    burgers = BurgerModel.objects.all()
    context =   {'item':burgers,'active_link':'burgers'}
    return render(request,'food/burger.html',context)