from django.db import models
from django.utils.translation import gettext_lazy as _
from reusable.basemodels import BaseModel
from django.conf import settings


class Coupon(BaseModel):
    product = models.ForeignKey(
        'Product', verbose_name=_("product"),
        on_delete=models.CASCADE,
        related_name='to_coupons'
    )
    profit = models.DecimalField(
        _("profit"),
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default=0
    )
    percentageـdiscount = models.DecimalField(
        _("percentageـdiscoun"),
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default=0
    )
    amountـdiscount = models.DecimalField(
        _("amountـdiscount"),
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default=0
    )

class Product(BaseModel):
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"), blank=True, null=True)
    price = models.DecimalField(
        _("price"),
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES
    )
    is_fragile = models.BooleanField(_("is_fragile"), default=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        Coupon.objects.create(product=self)
        return super().save(*args, **kwargs)
