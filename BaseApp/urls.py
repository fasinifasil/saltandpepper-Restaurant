from  django.urls import path
from  . import views
app_name='BaseApp'
urlpatterns=[
    path('',views.PizzaPage,name='pizzas'),
    path('burger',views.BurgerPage,name='burgers'),
    path('order',views.OrderPage,name='order'),
    path('success',views.successPage,name='success'),
    path('signup',views.signup,name='signup'),
    path('login',views.loginpage,name='login'),
    path('logout',views.LogOut,name='logout'),
]