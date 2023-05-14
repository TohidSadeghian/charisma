from rest_framework.routers import DefaultRouter
from .views import OrderRegisterViewSet


router = DefaultRouter()
router.register(r'register_order', OrderRegisterViewSet, basename='register_order')




