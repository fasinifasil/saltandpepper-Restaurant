from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PizzaModel(models.Model):
    PizzaName        =   models.CharField(max_length=20)
    PizzapriceM      =   models.DecimalField(max_digits=5,decimal_places=2)
    PizzapriceL      =   models.DecimalField(max_digits=5,decimal_places=2)
    PizzaImage       =   models.URLField()

    def __str__(self):
        return self.PizzaName
class BurgerModel(models.Model):
    BurgerName        =   models.CharField(max_length=20)
    BurgerpriceM      =   models.DecimalField(max_digits=5,decimal_places=2)
    BurgerpriceL      =   models.DecimalField(max_digits=5,decimal_places=2)
    BurgerImage       =   models.URLField()

    def __str__(self):
        return self.BurgerName

class OrderModel(models.Model):
    customer      =  models.ForeignKey(User,on_delete=models.CASCADE)
    itemNumber    =  models.CharField(max_length=60)
    bill          = models.DecimalField(max_digits=6,decimal_places=2)
    date          = models.DateField(auto_now_add=True)
    note          = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.itemNumber
class ItemModel(models.Model):
    order       =   models.ForeignKey(OrderModel,on_delete=models.CASCADE)
    name        =   models.CharField(max_length=100)
    price       =   models.DecimalField(max_digits=6,decimal_places=2)
    size        =   models.CharField(max_length=60)

    def __str__(self):
        return self.name