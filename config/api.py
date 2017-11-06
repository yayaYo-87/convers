from rest_framework.routers import DefaultRouter

from app.market.viewsets import CatalogViewSet, CategoryViewSet, BooksViewSet, ClothesViewSet, DvdViewSet, \
    SouvenirsViewSet

router = DefaultRouter()
router.register(r'catalog', CatalogViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'books', BooksViewSet)
router.register(r'clothes', ClothesViewSet)
router.register(r'dvd', DvdViewSet)
router.register(r'souvenirs', SouvenirsViewSet)
