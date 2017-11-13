from rest_framework import viewsets

from app.market.models import Catalog, Category, Goods
from app.market.serializers import CatalogSerializer, CategorySerializer, GoodsSerializer, GoodsDetailSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GoodsDetailSerializer
        return super(GoodsViewSet, self).get_serializer_class()