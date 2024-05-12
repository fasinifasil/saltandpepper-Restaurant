from  django.urls import path
from  . import views
app_name='BaseApp'
urlpatterns=[
    path('',views.PizzaPage,name='pizzas'),
    path('burger',views.BurgerPage,name='burgers'),
    path('order',views.OrderPage,name='order'),
<<<<<<< HEAD
    path('success',views.successPage,name='success'),
    path('signup',views.signup,name='signup'),
    path('login',views.loginpage,name='login'),
    path('logout',views.LogOut,name='logout'),
=======
>>>>>>> 111aed1a57b15be7570ca0c0d6d944ccb3d76964
]