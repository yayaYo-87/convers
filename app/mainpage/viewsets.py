from rest_framework import viewsets

from app.mainpage.models import Slider, LeftSlider, TopBanner, LeftBlog
from app.mainpage.serializers import TopSliderSerializer, LeftSliderSerializer, TopBannerSerializer, LeftBlogSerializer


class TopSliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = TopSliderSerializer


class TopBannerViewSet(viewsets.ModelViewSet):
    queryset = TopBanner.objects.all()
    serializer_class = TopBannerSerializer


class LeftSliderViewSet(viewsets.ModelViewSet):
    queryset = LeftSlider.objects.all()
    serializer_class = LeftSliderSerializer


class LeftBlogViewSet(viewsets.ModelViewSet):
    queryset = LeftBlog.objects.all()
    serializer_class = LeftBlogSerializer