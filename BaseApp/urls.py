from  django.urls import path
from  . import views
app_name='BaseApp'
urlpatterns=[
    path('',views.PizzaPage,name='pizzas'),
    path('burger',views.BurgerPage,name='burgers')
]