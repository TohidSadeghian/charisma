from django.db import models


class ShippingChoices(models.TextChoices):
        NORMAL = "normal_shipping"
        EXPRESS = "express_shipping"