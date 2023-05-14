from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, Coupon
from rest_framework.exceptions import ValidationError,NotAcceptable
from tests.base_tests import BaseTestsCreation


class TestViews(BaseTestsCreation):

    def test_usermodel_creation(self):
        product = self.create_productmodel()
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(product.__str__(), self.initial_data['name'])

    