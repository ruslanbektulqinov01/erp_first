from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Supplier, Warehouse, Product
from .serializers import SupplierSerializer, WarehouseSerializer, ProductSerializer
from rest_framework.permissions import AllowAny


class AllDataAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        suppliers = Supplier.objects.all()
        warehouses = Warehouse.objects.all()
        products = Product.objects.all()

        supplier_serializer = SupplierSerializer(suppliers, many=True)
        warehouse_serializer = WarehouseSerializer(warehouses, many=True)
        product_serializer = ProductSerializer(products, many=True)

        data = {
            'suppliers': supplier_serializer.data,
            'warehouses': warehouse_serializer.data,
            'products': product_serializer.data
        }

        return Response(data)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [AllowAny]


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
