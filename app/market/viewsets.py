from rest_framework import viewsets

from app.market.models import Catalog, Category, Books, Clothes, Dvd, Souvenirs
from app.market.serializers import CatalogSerializer, CategorySerializer, BooksSerializer, BooksDetailSerializer, \
    ClothesSerializer, ClothesDetailSerializer, DvdSerializer, DvdDetailSerializer, SouvenirsSerializer, \
    SouvenirsDetailSerializer


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


class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClothesDetailSerializer
        return super(ClothesViewSet, self).get_serializer_class()


class DvdViewSet(viewsets.ModelViewSet):
    queryset = Dvd.objects.all()
    serializer_class = DvdSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DvdDetailSerializer
        return super(DvdViewSet, self).get_serializer_class()


class SouvenirsViewSet(viewsets.ModelViewSet):
    queryset = Souvenirs.objects.all()
    serializer_class = SouvenirsSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SouvenirsDetailSerializer
        return super(SouvenirsViewSet, self).get_serializer_class()