# from django.urls import reverse
# from django.contrib.auth.models import User
# from rest_framework.test import APITestCase
# from products.models import Product, Coupon
# from reusable.utils import fake_generate
# from django.core.cache import cache
# from rest_framework.exceptions import ValidationError,NotAcceptable
# from decimal import Decimal


# class TestSetup(APITestCase):
   
#     def setUp(self) -> None:
#        self.initial_data = {}.fromkeys({'username','password', 'name', 'description'}, fake_generate())
#        self.quantity = 4
#        self.decimal_price = Decimal(70000.0)
#        return super().setUp()
    
#     def tearDown(self) -> None:
#         return super().tearDown()

# class TestProductModel(TestSetup):

#         def create_usermodel(self):
#             return User.objects.create_user(
#                 username = self.initial_data['username'],
#                 password = self.initial_data['password'],
#             )
#         def create_productmodel(self):
#             return Product.objects.create(
#                 name = self.initial_data['name'],
#                 description = self.initial_data['description'],
#                 price  = self.decimal_price,
#                 is_fragile = True
#             )

# class Order(BaseModel):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='orders',
#         verbose_name=_('user')
#     )
#     basket = models.ManyToManyField(Product, verbose_name=_("basket"), through='Basket')
#     is_closed = models.BooleanField(_("is_closed"), default=False)

#     def __str__(self):
#         return f'the order created by {self.user.username}'


# class Basket(BaseModel):
#     product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
#     order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE, related_name='order_baskets')
#     quantity = models.PositiveSmallIntegerField(_("quantity"))

    