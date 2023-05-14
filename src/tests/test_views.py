from datetime import timedelta
from django.urls import reverse
from tests.base_tests import BaseTestsCreation
from django.conf import settings
from rest_framework.exceptions import NotAuthenticated, PermissionDenied, AuthenticationFailed
class TestViews(BaseTestsCreation):

    def test_product_views(self):
        url = reverse("products-list")
        first_product = self.create_productmodel()
        second_product = self.create_productmodel()
        response = self.client.get(url)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['name'], first_product.name)

    def test_unathourized_user_basket(self):
        url = reverse("baskets-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code,400)
        # try:
        #     rs = self.client.get(url)
        # except Exception as e:
        #     print(e.args)
        # print(rs.status_code)
        # with self.assertRaises(self.client.errors) as cm:
        #     self.client.get(url)
            # self.assertEqual(cm.exception, response) # contex

    def test_user_can_add_product_to_basket(self):
        url = reverse("baskets-list")
        user = self.create_usermodel()
        self.client.force_login(user=user)
        product = self.create_productmodel()
        data = {"product": product.id, "quantity": self.quantity}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_user_can_register_order_less_than_five_hundreds(self):
        url = reverse("baskets-list")
        register_order_url = reverse("register_order-list")
        user = self.create_usermodel()
        self.client.force_login(user=user)
        product = self.create_productmodel()
        data = {"product": product.id, "quantity": self.quantity}
        self.client.post(url, data)
        response = self.client.post(register_order_url)
        self.assertEqual(response.status_code, 400)
    
    def test_user_can_register_order_in_forbidden_times(self):
        url = reverse("baskets-list")
        register_order_url = reverse("register_order-list")
        user = self.create_usermodel()
        self.client.force_login(user=user)
        product = self.create_productmodel()
        data = {"product": product.id, "quantity": self.quantity}
        self.client.post(url, data)
        settings.TIME_ZONE = "" + timedelta(hours=4, minutes=30)
        response = self.client.post(register_order_url)
        self.assertEqual(response.status_code, 400)




# register orders between 7, 8 

