from django.contrib import admin

from BaseApp.models import PizzaModel,BurgerModel
class displayPizza(admin.ModelAdmin):
    list_display = ['PizzaName','PizzapriceM','PizzapriceL']

admin.site.register(PizzaModel,displayPizza)
class displayBurger(admin.ModelAdmin):
    list_display = ['BurgerName','BurgerpriceM','BurgerpriceL']
admin.site.register(BurgerModel,displayBurger)