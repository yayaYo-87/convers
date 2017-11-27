from datetime import datetime

from rest_framework import mixins
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app.orders.models import Order, Cart, OrderGoods
from app.orders.serializers import OrderSerializer, OrderDetailSerializer, CartSerializer, OrderGoodsSerializer


class OrderViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = ()

    def perform_create(self, serializer):
        status_code = 'waiting'
        serializer.save(order_status=status_code)
        obj = serializer.save()
        cart = Cart.objects.filter(cookie=self.request.session.session_key).first()
        order_goods = OrderGoods.objects.filter(cart=cart, active=True)
        for order in order_goods:
            order.created_at = datetime.now()
            order.save()
        order_goods.update(cart=None, order=obj)
        cart.save()
        obj.save()
        OrderGoods.objects.filter(cart=cart, active=False).delete()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderDetailSerializer
        return super(OrderViewSet, self).get_serializer_class()

    @detail_route(methods=['post'])
    def change_status(self, request, pk=None):
        op = get_object_or_404(OrderGoods, pk=pk)
        op.save()
        return Response(OrderGoodsSerializer(instance=op).data)


class CartViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(cookie=self.request.session.session_key)


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

    @detail_route(methods=['post'])
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