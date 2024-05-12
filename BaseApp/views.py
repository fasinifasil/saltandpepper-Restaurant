import json
import random

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from BaseApp.models import PizzaModel, BurgerModel,ItemModel,OrderModel
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.

def randomOrderNumber(length):
    sample  ='ABCDEFGH0123456789';
    number0 =''.join((random.choice(sample) for i in range(length)))
    return number0
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



#
# @csrf_exempt
# def OrderPage(request):
#     request.session.set_expiry(0)
#     if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         request.session['note'] = request.POST.get('note')
#         request.session['order'] = request.POST.get('orders')
#         request.session['bill'] = request.POST.get('bill')
#         orders  =   json.loads(request.session['order'])
#         if request.user.is_authenticated:
#             order=OrderModel(customer=request.user,
#                              itemNumber=randomOrderNumber(6),
#                              bill= float(request.session['bill']),
#                              note= request.session['note'])
#             order.save()
#             for article in orders:
#                 item = ItemModel(order =  article,
#                                  name =article[0],
#                                  price =float(article[2]),
#                                  size = article[1],
#                                  )
#                 item.save()
#
#
#
#     context = {'active_link': 'orders'}
#
#
#     return render(request, 'food/order.html',context)
@csrf_exempt
def OrderPage(request):
    request.session.set_expiry(0)
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
        request.session['bill'] = request.POST.get('bill')
        orders = json.loads(request.session['order'])
        randomNum = randomOrderNumber(6)
        while OrderModel.objects.filter(itemNumber=randomNum).count() > 0:
            randomNum = randomOrderNumber(6)

        # Check if bill is set and is not None
        if 'bill' in request.session and request.session['bill'] is not None:
            bill = float(request.session['bill'])
        else:
            # Handle case where bill is not set or None
            bill = 0.0  # Set a default value or handle it according to your logic

        if request.user.is_authenticated:
            order = OrderModel(customer=request.user,
                               itemNumber=randomOrderNumber(6),
                               bill=bill,  # Use the updated bill value here
                               note=request.session['note'])
            order.save()
            request.session['orderNum']=order.itemNumber
            for article in orders:
                item = ItemModel(order=order,  # Use the created order instance
                                 name=article[0],
                                 price=float(article[2]),
                                 size=article[1])
                item.save()

    context = {'active_link': 'orders'}
    return render(request, 'food/order.html', context)


def successPage(request):
    orderNum=request.session['orderNum']
    bill= request.session['bill']
    items =ItemModel.objects.filter(order__itemNumber  =orderNum)

    context={'orderNum':orderNum,'bill':bill,'items':items}
    return render(request,'food/success.html',context)

def signup(request):
    context={}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context['form']=form
    else:
        form = NewUserForm()
        context['form'] = form

    return render(request, 'food/signup.html',context)

def loginpage(request):
    context = {'active_link': 'login'}
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request,username=username,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, "Invalid credentials")
    return render(request,'food/login.html',context)

def LogOut(request):
    logout(request)
    return redirect('index')