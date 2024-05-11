from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from BaseApp.models import PizzaModel, BurgerModel
from django.http import JsonResponse

# Create your views here.
def IndexPage(request):
    request.session.set_expiry(0)

    context = {'active_link': 'index'}
    return render(request, 'food/index.html', context)

def PizzaPage(request):
    request.session.set_expiry(0)

    pizzas = PizzaModel.objects.all()
    context = {'item': pizzas, 'active_link': 'pizzas'}
    return render(request, 'food/pizza.html', context)

def BurgerPage(request):
    request.session.set_expiry(0)

    burgers = BurgerModel.objects.all()
    context = {'item': burgers, 'active_link': 'burgers'}
    return render(request, 'food/burger.html', context)




@csrf_exempt
def OrderPage(request):
    request.session.set_expiry(0)
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')

    context = {'active_link': 'orders'}


    return render(request, 'food/order.html',context)

def successPage(request):
    order=request.session['order']
    context={'order':order}
    return render(request,'food/success.html',context)