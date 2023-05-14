from rest_framework import serializers
from ..models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ('invoice_detail',)

    def create(self, validated_data):
        obj =  super().create(validated_data)
        order = validated_data['order']
        order.is_closed = True
        order.save()
        return obj
