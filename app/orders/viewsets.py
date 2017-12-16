from datetime import datetime

from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet

from app.orders.models import Order, Cart, OrderGoods, Promocode
from app.orders.serializers import OrderSerializer, OrderDetailSerializer, CartSerializer, OrderGoodsSerializer, \
    PromocodeSerializer


class OrderViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = ()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = Cart.objects.filter(cookie=self.request.session.session_key).first()
        order_goods = OrderGoods.objects.filter(cart=cart, active=True).all()
        print(order_goods)
        if order_goods.exists():
            self.perform_create(serializer, cart=cart, order_goods=order_goods)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'error':'No goods in a cart'})

    def perform_create(self, serializer, **kwargs):
        status_code = 'waiting'
        cart = kwargs.get('cart')
        order_goods = kwargs.get('order_goods')
        serializer.save(order_status=status_code)
        obj = serializer.save()
        for order in order_goods:
            order.created_at = datetime.now()
            order.save()
        order_goods.update(cart=None, order=obj)
        cart.save()
        obj.save()
        OrderGoods.objects.filter(cart=cart, active=False).delete()
        return Response(obj.id)

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderDetailSerializer
        return super(OrderViewSet, self).get_serializer_class()


class CartViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = ()

    def get_queryset(self):
        return Cart.objects.filter(cookie=self.request.session.session_key)

    @detail_route(methods=['post'], url_name='use_promocode', url_path='use_promocode/(?P<code>[a-z0-9]+)')
    def use_promocode(self, request, pk=None, code=None):
        cart = get_object_or_404(Cart, pk=pk, cookie=self.request.session.session_key)
        promocode = Promocode.objects.filter(code=code).first()
        if promocode:
            total_discount = cart.price * promocode.discount / 100
            cart.total_discount = total_discount
            cart.save()
            return Response(CartSerializer(instance=cart).data)
        else:
            return Response({'error':'No such promocode'})

    @detail_route(methods=['post'])
    def check_goods(self, request, pk=None):
        # cart = Cart.objects.filter(cookie=self.request.session.session_key).first()
        cart = get_object_or_404(Cart, pk=pk)
        if cart.cart_goods.all():
            return Response({'true'})
        else:
            return Response({'false'})


class PromocodeViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer


class OrderGoodsViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = OrderGoods.objects.all()
    serializer_class = OrderGoodsSerializer
    authentication_classes = ()

    def perform_create(self, serializer):
        cart = Cart.objects.filter(cookie=self.request.session.session_key).first()
        # old_jibbitz = OrderGoods.objects.filter(
        #     cart=cart,
        #     jibbitz_id=self.request.data['jibbitz'],
        # ).all()
        # for old_jibbitz_item in old_jibbitz:
        #     if old_jibbitz_item:
        #         count = old_jibbitz_item.count
        #         if not old_jibbitz_item.active:
        #             old_jibbitz_item.active = True
        #         else:
        #             old_jibbitz_item.count = count + 1
        #             old_jibbitz_item.save()
        #         cart.save()
        #         return
        cart.save()
        serializer.save()

    @detail_route(methods=['post'])
    def inc(self, request, pk=None):
        cart = Cart.objects.filter(cookie=self.request.session.session_key).first()
        op = get_object_or_404(OrderGoods, pk=pk)
        count = op.count
        op.count = count + 1
        op.save()
        cart.save()
        return Response(OrderGoodsSerializer(instance=op).data)

    @detail_route(methods=['post'])
    def dec(self, request, pk=None):
        cart = Cart.objects.filter(cookie=self.request.session.session_key).first()
        op = get_object_or_404(OrderGoods, pk=pk)
        count = op.count
        if count > 1:
            op.count = count - 1
            op.save()
            cart.save()
        return Response(OrderGoodsSerializer(instance=op).data)

    @detail_route(methods=['post'], )
    def deactivate(self, request, pk=None):
        cart = Cart.objects.filter(cookie=self.request.session.session_key).first()
        op = get_object_or_404(OrderGoods, pk=pk)
        op.active = False
        op.save()
        cart.save()
        return Response(OrderGoodsSerializer(instance=op).data)

    @detail_route(methods=['post'])
    def activate(self, request, pk=None):
        cart = Cart.objects.filter(cookie=self.request.session.session_key).first()
        op = get_object_or_404(OrderGoods, pk=pk)
        op.active = True
        op.save()
        cart.save()
        return Response(OrderGoodsSerializer(instance=op).data)
