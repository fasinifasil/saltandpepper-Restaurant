from django.test import TestCase
from django.urls import reverse

from BaseApp.models import PizzaModel


# Create your tests here.
# class homePageTestCase(TestCase):
#     def test_home_page(self):
#             self.assertEqual('test1','test1')
class homePageTestCase(TestCase):
    def test_home_page(self):
        response    =   self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
class pizzaPageTestCase(TestCase):
    def test_newPizza_added(self):
        countPizza    =   PizzaModel.objects.count()
        PizzaModel.objects.create(PizzaName='Italian Bbq Pizza',PizzapriceM=280,PizzapriceL=500,PizzaImage='https://img.freepik.com/premium-photo/bbq-pizza-topped-with-slices-spicy-italian-sausage-roasted-red-peppers-caramelized-onions_198067-250074.jpg')

        self.assertEqual(PizzaModel.objects.count(),countPizza+1)