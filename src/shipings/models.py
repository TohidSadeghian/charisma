from django.db import models
from django.utils.translation import gettext_lazy as _
from reusable.basemodels import BaseModel
from .choices import ShippingChoices
from orders.models import Basket


class Shipping(BaseModel):
    basket = models.ForeignKey(
        Basket,
        verbose_name=_("basket"),
        on_delete=models.CASCADE,
        related_name='shiptobasket',
    )
    type = models.CharField(
        _("type"),
        max_length=30,
        choices=ShippingChoices.choices
    )
    is_done = models.BooleanField(_("is_done"), default=False)
