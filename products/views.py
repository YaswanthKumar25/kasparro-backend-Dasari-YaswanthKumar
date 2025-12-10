from rest_framework import viewsets, filters
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    APIs:
    - GET /api/products/        -> list with pagination, search, ordering
    - GET /api/products/{id}/   -> single product
    """
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "category"]
    ordering_fields = ["price", "title"]
