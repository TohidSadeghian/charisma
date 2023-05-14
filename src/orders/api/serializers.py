from rest_framework import serializers
from ..models import Basket
from django.db import connection


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ('id', 'order', 'product', 'quantity')
        extra_kwargs = {'order' :{'read_only': True}}

    # representation -->  order detail
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['price'] = instance.product.price
        return representation

class EditBasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ('id', 'order', 'product', 'quantity')
        read_only_fields = ('id', 'order', ' product')

