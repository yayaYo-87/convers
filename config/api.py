from rest_framework.routers import DefaultRouter

from app.mainpage.viewsets import TopSliderViewSet, TopBannerViewSet, LeftSliderViewSet, LeftBlogViewSet
from app.market.viewsets import CatalogViewSet, CategoryViewSet, GoodsViewSet, MainGoodsViewSet
from app.orders.viewsets import OrderViewSet, CartViewSet

router = DefaultRouter()
router.register(r'catalog', CatalogViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'goods', GoodsViewSet)
router.register(r'main_goods', MainGoodsViewSet)

router.register(r'order', OrderViewSet)
router.register(r'cart', CartViewSet)

router.register(r'top_slider', TopSliderViewSet)
router.register(r'top_banner', TopBannerViewSet)
router.register(r'left_slider', LeftSliderViewSet)
router.register(r'left_blog', LeftBlogViewSet)
