from rest_framework import viewsets

from app.market.models import Catalog, Category, Books
from app.market.serializers import CatalogSerializer, CategorySerializer, BooksSerializer, BooksDetailSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BooksDetailSerializer
        return super(BooksViewSet, self).get_serializer_class()