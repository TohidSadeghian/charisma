from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .serializers import InvoiceSerializer
from django.shortcuts import get_object_or_404
from orders.models import Order
from ..models import Invoice


class OrderRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        order = get_object_or_404(Order, user=user, is_closed=False)
        serializer.validated_data.update(order=order)
        serializer.save()

