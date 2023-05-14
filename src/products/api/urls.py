from rest_framework.routers import DefaultRouter
from .views import ProductViewSets


router = DefaultRouter()
router.register(r'products', ProductViewSets, basename="products")



