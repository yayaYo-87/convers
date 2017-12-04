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
    id = json.loads(request.body.decode("utf-8"))['id']
    order = Order.objects.filter(id=id).first()
    json_data = {}
    if order:
        json_data['TerminalKey'] = '1511862369151DEMO'
        json_data['Amount'] = int(order.total_delivery) * 100 + int(order.total) * 100
        json_data['OrderId'] = order.id
        json_data['Description'] = 'Классические беседы'
        json_data.setdefault('DATA', {})
        json_data['DATA']['Phone'] = order.phone
        json_data['DATA']['Email'] = order.email
        json_data.setdefault('Receipt', {})
        json_data['Receipt']['Email'] = order.email
        json_data['Receipt']['Phone'] = order.phone
        json_data['Receipt']['Taxation'] = 'usn_income'
        json_data['Receipt'].setdefault('Items', [])
        for i in order.order_goods.all():
            item = {
                'Name':i.goods.name,
                'Price':int(i.goods.price)*100,
                'Quantity':i.count,
                'Amount':int(i.goods.price) * 100 * i.count,
                'Tax':'none'
            }
            json_data['Receipt']['Items'].append(item)
        delivery = {
            'Name': 'Доставка',
            'Price': int(order.total_delivery) * 100,
            'Quantity': 1,
            'Amount': int(order.total_delivery) * 100,
            'Tax': 'none'
        }
        json_data['Receipt']['Items'].append(delivery)
        print(json_data)

    headers = {
        'content-type': 'application/json',
    }
    path = 'https://securepay.tinkoff.ru/v2/Init'
    f = requests.post(path, headers=headers, json=json_data)

    return HttpResponse(f.content)


@require_http_methods(["POST"])
@csrf_exempt
def cancel_pay(request):
    path = 'https://securepay.tinkoff.ru/v2/Cancel'
    f = requests.post(path)

    return HttpResponse(f.content)


@require_http_methods(["POST"])
@csrf_exempt
def resend_pay(request):
    path = 'https://securepay.tinkoff.ru/v2/Resend'
    f = requests.post(path)

    return HttpResponse(f.content)


def shiptorg_post(order):
    print(order)
    # headers = {
    #     'content-type': 'application/json',
    #     'x-authorization-token': '4b8015c64d6c260d377374edecda8b54027c78ca',
    # }
    # path = 'https://api.shiptor.ru/shipping/v1'
    # f = requests.post(path, headers=headers, json=order)
    # print(f.json())

    # return HttpResponse(f.content)
    return HttpResponse('2')


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
    print(pure_value)

    generated_token = sha256(pure_value.encode('ascii')).hexdigest()
    return generated_token == received_token


@require_http_methods(["POST"])
@csrf_exempt
def get_payment_status(request):
    params = json.loads(request.body.decode("utf-8"))
    id = params.get('OrderId')
    status = params.get('Status')
    print('status = ', status)
    # convert python booleans to js string
    # e.g True to "true"
    params = {k: str(v).lower() if isinstance(v, bool) else v for k, v in params.items()}
    token_valid = check_token(params)

    if token_valid:
        order = get_object_or_404(Order, id=id)
        if order:
            shiptorg_post(order)
        order.order_status = 'confirmed' if status == 'CONFIRMED' else 'cancel'
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
