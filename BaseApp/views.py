from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from BaseApp.models import PizzaModel, BurgerModel
from django.http import JsonResponse

# Create your views here.
def IndexPage(request):
    context = {'active_link': 'index'}
    return render(request, 'food/index.html', context)

def PizzaPage(request):
    pizzas = PizzaModel.objects.all()
    context = {'item': pizzas, 'active_link': 'pizzas'}
    return render(request, 'food/pizza.html', context)

def BurgerPage(request):
    burgers = BurgerModel.objects.all()
    context = {'item': burgers, 'active_link': 'burgers'}
    return render(request, 'food/burger.html', context)




@csrf_exempt
def OrderPage(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        note = request.POST.get('note')
        print(note)  # Just for debugging, remove this line in production
        # Process the request here
        return JsonResponse({'message': 'Order received successfully'})  # Send a JSON response

    return render(request, 'food/order.html')

