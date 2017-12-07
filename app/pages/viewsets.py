from rest_framework import viewsets

from app.pages.models import Page, PageFAQ
from app.pages.serializers import PageSerializer, PageFAQSerializer


class PageViewset(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'


class TopPageViewset(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Page.objects.filter(show_top=True).distinct()


class BottomPageViewset(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Page.objects.filter(show_bottom=True).distinct()


class PageFAQViewset(viewsets.ModelViewSet):
    queryset = PageFAQ.objects.all()
    serializer_class = PageFAQSerializer
    lookup_field = 'slug'