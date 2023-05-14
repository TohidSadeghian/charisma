from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from reusable.basemodels import BaseModel
from products.models import Product

  
class Order(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name=_('user')
    )
    basket = models.ManyToManyField(Product, verbose_name=_("basket"), through='Basket')
    is_closed = models.BooleanField(_("is_closed"), default=False)

    def __str__(self):
        return f'the order created by {self.user.username}'


class Basket(BaseModel):
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE, related_name='order_baskets')
    quantity = models.PositiveSmallIntegerField(_("quantity"))

    