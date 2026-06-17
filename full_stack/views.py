# views.py
from rest_framework.generics import ListCreateAPIView

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
