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

