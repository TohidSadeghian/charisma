from reusable.basemodels import BaseModel
from django.db import models
from orders.models import Order, Basket
from shipings.models import Shipping
from shipings.choices import ShippingChoices
from django.utils.translation import gettext_lazy as _
from django.db.models import F
from django.db import transaction
from rest_framework.exceptions import ValidationError
from django.conf import settings
from .messages import Messages


class Invoice(BaseModel):
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE)

    def check_total_price(self, total_price):
        if total_price < settings.MIN_TOTAL_PRICE:
            raise ValidationError({
                'error' : Messages.MIN_TOTAL_PRICE.value.format(settings.MIN_TOTAL_PRICE)
            })

    def shiping_details(self, shiping):
        details = list(map(lambda x : {'id':x.pk, 'basket':x.basket.pk, 'type':x.type}, shiping))
        return details

    def calculate_total_price(self, products_detail):
            total_price = sum(
                map(
                    lambda x:(x['price'] - x['price'] * x['percentageـdiscount']) + x['profit'] - x['amountـdiscount'],
                    products_detail
                )
            )
            return total_price

    with transaction.atomic():
        # try except toman

        @property
        def invoice_detail(self):
            products_detail = Basket.objects.filter(order=self.order).values(
                'product',
                price=F('product__price'),
                profit=F('product__to_coupons__profit'),
                percentageـdiscount=F('product__to_coupons__percentageـdiscount'),
                amountـdiscount=F('product__to_coupons__amountـdiscount')
            )
            total_price = self.calculate_total_price(products_detail=products_detail)
            self.check_total_price(total_price=total_price)
            baskets = Basket.objects.select_related('product')
            shiping = Shipping.objects.bulk_create(
                Shipping(
                    basket=basket,
                    type=ShippingChoices.EXPRESS.value if basket.product.is_fragile else ShippingChoices.NORMAL.value
                )
                for basket in baskets
            )
            return {
               'products_detail' : products_detail,
               'total_price' : total_price,
               'shiping' : self.shiping_details(shiping=shiping)
            }
        
