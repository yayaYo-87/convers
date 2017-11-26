from django.http import HttpResponse
from django.http import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from app.orders.models import Cart, OrderGoods
import requests


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        data = super(IndexView, self).get(*args, **kwargs)
        if self.request.session.is_empty():
            self.request.session.create()
        if not Cart.objects.filter(cookie=self.request.session.session_key):
            cart = Cart.objects.create(
                cookie=self.request.session.session_key
            )
        else:
            cart = Cart.objects.filter(cookie=self.request.session.session_key).first()
        if self.request.session.session_key:
            OrderGoods.objects.filter(
                cart=cart, active=False).delete()
        return data


@require_http_methods(["POST"])
@csrf_exempt
def init_pay(request):
    json_data = json.loads(request.body.decode("utf-8"))['json']
    headers = {
        'content-type': 'application/json',
    }
    path = 'https://securepay.tinkoff.ru/v2/Init'
    f = requests.post(path, headers=headers, json=json_data)
    # print(f.json())

    return HttpResponse(f.content)


@require_http_methods(["POST"])
@csrf_exempt
def cancel_pay(request):
    path = 'https://securepay.tinkoff.ru/v2/Cancel'
    f = requests.post(path)

    return HttpResponse(f.content)


@require_http_methods(["POST"])
@csrf_exempt
def get_state_pay(request):
    path = 'https://securepay.tinkoff.ru/v2/Cancel'
    f = requests.post(path)

    return HttpResponse(f.content)


@require_http_methods(["POST"])
@csrf_exempt
def resend_pay(request):
    path = 'https://securepay.tinkoff.ru/v2/Resend'
    f = requests.post(path)

    return HttpResponse(f.content)


def get_csrf_token(request):
    token = django.middleware.csrf.get_token(request)
    return JsonResponse({'token': token})


@require_http_methods(["POST"])
@csrf_protect
def shiptorg(request):
    json_data = json.loads(request.body.decode("utf-8"))['json']
    token = json.loads(request.body.decode("utf-8"))['token']
    headers = {
        'content-type': 'application/json',
        'x-authorization-token': '4b8015c64d6c260d377374edecda8b54027c78ca',
        'X-CSRFToken': token
    }
    path = 'https://api.shiptor.ru/shipping/v1'
    f = requests.post(path, headers=headers, json=json_data)
    # print(f.json())

    return HttpResponse(f.content)
