import json
from _sha256 import sha256

import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from app.orders.models import Cart, OrderGoods, Order


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


def check_token(params):
    """
    https://oplata.tinkoff.ru/landing/develop/plug/tokens
    """
    received_token = params.pop('Token')
    params['Password'] = settings.TINKOFF_PASSWORD
    items_list = sorted(params.items(), key=lambda x: x[0])

    pure_value = ''
    for item in items_list:
        pure_value = '%s%s' % (pure_value, item[1])

    generated_token = sha256(pure_value.encode('ascii')).hexdigest()
    return generated_token == received_token


@require_http_methods(["POST"])
@csrf_exempt
def get_payment_status(request):
    params = json.loads(request.body.decode("utf-8"))
    id = params.get('OrderId')
    status = params.get('Status')
    # convert python booleans to js string
    # e.g True to "true"
    params = {k: str(v).lower() if isinstance(v, bool) else v for k, v in params.items()}
    token_valid = check_token(params)
    
    if token_valid:
        order = get_object_or_404(Order, id=id)
        order.status = 'confirmed' if status == 'CONFIRMED' else 'cancel'
        order.save()
        return HttpResponse(status=200, content='OK')
    
    return HttpResponse(status=403, content='Incorrect token')


@require_http_methods(["POST"])
@csrf_exempt
def shiptorg(request):
    json_data = json.loads(request.body.decode("utf-8"))['json']
    headers = {
        'content-type': 'application/json',
        'x-authorization-token': '4b8015c64d6c260d377374edecda8b54027c78ca',
    }
    path = 'https://api.shiptor.ru/shipping/v1'
    f = requests.post(path, headers=headers, json=json_data)
    # print(f.json())

    return HttpResponse(f.content)
