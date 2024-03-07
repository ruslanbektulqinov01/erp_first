from rest_framework import routers
from .views import SupplierViewSet, WarehouseViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'warehouses', WarehouseViewSet)
router.register(r'products', ProductViewSet)
