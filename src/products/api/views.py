from .serializers import ProductSerializer
from ..models import *
from rest_framework import viewsets, mixins


class ProductViewSets(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
