import json
from _sha256 import sha256

import requests
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
# from easy_pdf.views import PDFTemplateView

from app.orders.models import Cart, OrderGoods, Order, CoursesOrdersCoursesorder, CoursesOrdersOrdertickets, \
    DirectorAdmitDirectoradmit, DirectorAdmitParentsadmit, DirectorAdmitParentletter, \
    DirectorAdmitParentsadmitChildrenDirector, DirectorAdmitDirectorschild


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
        json_data['TerminalKey'] = settings.TINKOFF_TERMINAL_KEY
        json_data['Amount'] = int(order.total_delivery) * 100 + int(order.total) * 100 - int(order.total_discount) * 100
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
        if order.total_delivery:
            delivery = {
                'Name': 'Доставка',
                'Price': int(order.total_delivery) * 100,
                'Quantity': 1,
                'Amount': int(order.total_delivery) * 100,
                'Tax': 'none'
            }
            json_data['Receipt']['Items'].append(delivery)
        if order.total_discount:
            promocode = {
                'Name': 'Скидка по промокоду',
                'Price': -(int(order.total_discount) * 100),
                'Quantity': 1,
                'Amount': -int(order.total_discount) * 100,
                'Tax': 'none'
            }
            json_data['Receipt']['Items'].append(promocode)
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
    length = 0
    width = 0
    height = 0
    weight = 0
    products = []
    for i in order.order_goods.all():
        item = {
            'shopArticle':i.goods.articul,
            'count':i.count,
            'price':i.goods.price
        }
        products.append(item)
        if length < i.goods.length:
            length = float(i.goods.length)
        if weight < i.goods.weight:
            width = float(i.goods.width)
        height += float(i.goods.height)
        weight += float(i.goods.weight)
    json_data = {}
    json_data['id'] = 'JsonRpcClient.js'
    json_data['jsonrpc'] = '2.0'
    json_data['method'] = 'addPackage'
    json_data.setdefault('params', {})
    json_data['params']['length'] = length
    json_data['params']['width'] = width
    json_data['params']['height'] = height
    json_data['params']['weight'] = weight
    json_data['params']['cod'] = 0
    json_data['params']['declared_cost'] = 10 if order.total < 12000 else 1000
    json_data['params'].setdefault('departure', {})
    json_data['params']['departure']['shipping_method'] = order.shipping_id
    if not order.delivery_point == '0':
        json_data['params']['departure']['delivery_point'] = order.delivery_point
    json_data['params']['departure']['comment'] = order.comment
    json_data['params']['departure'].setdefault('address', {})
    json_data['params']['departure']['address']['country'] = 'RU'
    json_data['params']['departure']['address']['name'] = order.first_name
    json_data['params']['departure']['address']['surname'] = order.last_name
    json_data['params']['departure']['address']['receiver'] = order.last_name + ' ' + order.first_name
    json_data['params']['departure']['address']['email'] = order.email
    json_data['params']['departure']['address']['phone'] = order.phone
    json_data['params']['departure']['address']['postal_code'] = order.index
    json_data['params']['departure']['address']['administrative_area'] = order.administrative_area
    json_data['params']['departure']['address']['settlement'] = order.settlement
    json_data['params']['departure']['address']['street'] = order.address
    json_data['params']['departure']['address']['house'] = order.home
    json_data['params']['departure']['address']['apartment'] = order.apartment
    json_data['params']['departure']['address']['address_line_1'] = order.administrative_area + ', ' + order.settlement + \
        ', ' + order.address + ', ' + order.home + ', ' + order.apartment
    json_data['params']['departure']['address']['kladr_id'] = order.kladr_id
    json_data['params']['products'] = products
    headers = {
        'content-type': 'application/json',
        'x-authorization-token': settings.SHIPTOR_TOKEN,
    }
    path = 'https://api.shiptor.ru/shipping/v1'
    f = requests.post(path, headers=headers, json=json_data)
    print('json_data: ', json_data)
    print('Shiptor responce: ', json.loads(f.text))

    return HttpResponse(f.content)


def email_view(order):
    if order:
        subject = "Оформление посылки на доставку"
        to = [order.email]
        from_email = 'info@classicalbooks.ru'

        total = order.total + order.total_delivery - order.total_discount

        ctx = {
            'order': order,
            'total': total
        }

        message = get_template('email/email.html').render(ctx)
#         print(message)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()

        return HttpResponse({'response': 1})


def email_view_courses(order):
    if order:
        subject = "Оформление cсылок на билеты"
        to = [order.email]
        from_email = 'info@classicalbooks.ru'

        total = order.total
        tickets = CoursesOrdersOrdertickets.objects.filter(order_id=order.id).all()
        ids = []
        for i in tickets:
            ids.append(i.ids)

        ctx = {
            'order': order,
            'total': total,
            'tickets': tickets
        }

        message = get_template('email/courses_email.html').render(ctx)
#         print(message)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()

        return HttpResponse({'response': 1})


def email_view_admit(order):
    print('Подтверждение, отправка письма')
    if order:
        director_subject = "Вы успешно зарегистрировались"
        director_to = [order.email]
        from_email = 'info@classicalbooks.ru'

        ctx = {
            'order': order,
        }

        director_message = get_template('email/courses_director_email.html').render(ctx)
        director_msg = EmailMessage(
            director_subject,
            director_message,
            to=director_to,
            from_email=from_email
        )
        director_msg.content_subtype = 'html'
        director_msg.send()

    return HttpResponse({'response': 1})


def email_view_parent_admit(order):
    print('Подтверждение, отправка письма родителям')
    letter = DirectorAdmitParentletter.objects.filter(active=True).first()
    if order:
        director_subject = "Вы успешно зарегистрировались"
        parent_to = [order.email]
        from_email = 'info@classicalbooks.ru'

        children = []
        child = DirectorAdmitParentsadmitChildrenDirector.objects.filter(parentsadmit=order.id).all()
        for i in child:
            children.append(DirectorAdmitDirectorschild.objects.filter(id=i.directorschild.id).first())

        ctx = {
            'order': order,
            'letter': letter,
            'children': children,
        }

        parent_message = get_template('email/courses_parent_email.html').render(ctx)
        parent_msg = EmailMessage(
            director_subject,
            parent_message,
            to=parent_to,
            from_email=from_email
        )
        parent_msg.content_subtype = 'html'
        parent_msg.send()

        director_message = get_template('email/courses_parent_email.html').render(ctx)
        director_msg = EmailMessage(
            director_subject,
            director_message,
            to=[order.community.email, ],
            from_email=from_email
        )
        director_msg.content_subtype = 'html'
        director_msg.send()

    return HttpResponse({'response': 1})


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
    print('tinkov_request = ', params)
    # convert python booleans to js string
    # e.g True to "true"
    params = {k: str(v).lower() if isinstance(v, bool) else v for k, v in params.items()}
    token_valid = check_token(params)

    if token_valid:
        # Проверка откуда пришел заказ по его id
        if str(id).find('courses_') == 0:
            order = CoursesOrdersCoursesorder.objects.filter(extra_id=str(id)).first()
            order.order_status = 'confirmed' if status == 'CONFIRMED' else 'cancel'
            order.save()
            if order.order_status == 'confirmed':
                email_view_courses(order)
            print('order.id: ', order.id, ', order_status: ', order.order_status)
        elif str(id).find('admit_') == 0:
            admit = DirectorAdmitDirectoradmit.objects.filter(extra_id=str(id)).first()
            admit.order_status = 'confirmed' if status == 'CONFIRMED' else 'cancel'
            admit.save()
            if admit.order_status == 'confirmed':
                email_view_admit(admit)
            print('admit.id: ', admit.id, ', order_status: ', admit.order_status)
        elif str(id).find('parent_') == 0:
            admit = DirectorAdmitParentsadmit.objects.filter(extra_id=str(id)).first()
            admit.order_status = 'confirmed' if status == 'CONFIRMED' else 'cancel'
            admit.save()
            if admit.order_status == 'confirmed':
                email_view_parent_admit(admit)
            print('admit.id: ', admit.id, ', order_status: ', admit.order_status)
        else:
            print('convers_id: ', id)
            order = get_object_or_404(Order, id=id)
            order.order_status = 'confirmed' if status == 'CONFIRMED' else 'cancel'

            if order.order_status == 'confirmed' and order.send_to_shiptor == False:
                if not order.order_delivery == 'without':
                    shiptorg_post(order)
                    order.send_to_shiptor = True
                order.save()
                email_view(order)
            else:
                order.save()
        return HttpResponse(status=200, content='OK')
    
    return HttpResponse(status=403, content='Incorrect token')


@require_http_methods(["POST"])
@csrf_exempt
def shiptorg(request):
    json_data = json.loads(request.body.decode("utf-8"))['json']
    headers = {
        'content-type': 'application/json',
        'x-authorization-token': settings.SHIPTOR_TOKEN,
    }
    path = 'https://api.shiptor.ru/shipping/v1'
    f = requests.post(path, headers=headers, json=json_data)
    # print(f.json())

    return HttpResponse(f.content)


@require_http_methods(["POST"])
@csrf_exempt
def feedback_view(request, *args, **kwargs):
    subject = "Сообщение от пользователя"
    to = ['info@classicalbooks.ru', ]
    from_email = 'info@classicalbooks.ru'

    data = request.POST.copy()

    ctx = {
        'data': data,
    }

    message = get_template('email/feedback.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponse({'response': 1})
