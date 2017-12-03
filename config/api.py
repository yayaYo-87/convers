from rest_framework.routers import DefaultRouter

from app.mainpage.viewsets import TopSliderViewSet, TopBannerViewSet, LeftSliderViewSet, LeftBlogViewSet, \
    LeftAboutViewSet
from app.market.viewsets import CatalogViewSet, CategoryViewSet, GoodsViewSet, MainGoodsViewSet
from app.orders.viewsets import OrderViewSet, CartViewSet, OrderGoodsViewSet
from app.pages.viewsets import PageViewset, PageFAQViewset

router = DefaultRouter()
router.register(r'catalog', CatalogViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'goods', GoodsViewSet)
router.register(r'main_goods', MainGoodsViewSet)

router.register(r'order', OrderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'order_goods', OrderGoodsViewSet)

router.register(r'top_slider', TopSliderViewSet)
router.register(r'top_banner', TopBannerViewSet)
router.register(r'left_slider', LeftSliderViewSet)
router.register(r'left_about', LeftAboutViewSet)
router.register(r'left_blog', LeftBlogViewSet)

router.register(r'pages', PageViewset)
router.register(r'faq_page', PageFAQViewset)
