from reusable.baseviews import ModelViewSet
from ..models import Basket, Order
from .serializers import BasketSerializer, EditBasketSerializer
from reusable.paginations import CustomPagination
from .permissions import OrderPermission


class BasketViewSet(ModelViewSet):
    permission_classes = (OrderPermission,)
    pagination_class = CustomPagination
    queryset = Basket.objects.select_related()
    http_method_names = ('post', 'get', 'patch', 'delete')

    def get_queryset(self):
        qs= super().get_queryset()
        return qs.filter(order__user=self.request.user)
      
    def get_serializer_class(self):
        if self.action == 'partial_update':
            return EditBasketSerializer
        return BasketSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        order, _ = Order.objects.get_or_create(user=user, is_closed=False)
        serializer.validated_data.update(order=order)
        super().perform_create(serializer)

