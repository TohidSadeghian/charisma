from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.test import Client
from products.models import Product, Coupon
from reusable.utils import fake_generate
from decimal import Decimal


class TestSetup(APITestCase):
   
    def setUp(self) -> None:
       self.initial_data = {}.fromkeys({'username','password', 'name', 'description'}, fake_generate())
       self.decimal_price = Decimal(700.0)
       self.quantity = 4
       return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

class BaseTestsCreation(TestSetup):

    def create_usermodel(self):
            return User.objects.create_user(
                username = self.initial_data['username'],
                password = self.initial_data['password'],
            )

    def create_productmodel(self):
        return Product.objects.create(
            name = self.initial_data['name'],
            description = self.initial_data['description'],
            price  = self.decimal_price,
            is_fragile = True
        )


