from rest_framework import viewsets

from app.pages.models import Page, PageFAQ
from app.pages.serializers import PageSerializer, PageFAQSerializer


class PageViewset(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'


class PageFAQViewset(viewsets.ModelViewSet):
    queryset = PageFAQ.objects.all()
    serializer_class = PageFAQSerializer
    lookup_field = 'slug'