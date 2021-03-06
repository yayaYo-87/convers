"""convers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from config.api import router

from app.market.views import IndexView, init_pay, cancel_pay, resend_pay, shiptorg, \
    get_payment_status, email_view, feedback_view
from config import settings

urlpatterns = [
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^admin/', admin.site.urls),
    url(r'^_nested_admin/', include('nested_admin.urls')),
    url(r'^init_pay/$', init_pay, name='init_pay'),
    url(r'^cancel_pay/$', cancel_pay, name='cancel_pay'),
    url(r'^resend_pay/$', resend_pay, name='resend_pay'),
    url(r'^email_view/$', email_view, name='email_view'),
    url(r'^feedback_view/$', feedback_view, name='feedback_view'),
    url(r'^payment_status/$', get_payment_status, name='get_payment_status'),
    url(r'^shiptorg/$', shiptorg, name='shiptorg'),
    url(r'^[a-z]*_?/?[a-z]*_?/?[0-9]*_?/?[0-9]*$', IndexView.as_view(), name='index'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
