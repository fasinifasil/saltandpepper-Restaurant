from  django.urls import path
from  . import views
app_name='BaseApp'
urlpatterns=[
    path('pizza',views.PizzaPage,name='pizza')
]