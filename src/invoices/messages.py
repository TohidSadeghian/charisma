from enum import Enum
from django.utils.translation import gettext_lazy as _ 


class Messages(Enum):
    MIN_TOTAL_PRICE = _("The total price should not be less than {}")