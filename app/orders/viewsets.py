from datetime import datetime

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app.orders.models import Order, Cart, OrderGoods
from app.orders.serializers import OrderSerializer, OrderDetailSerializer


class OrderViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset =  Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = ()

    def perform_create(self, serializer):
        status_code = 'waiting' if self.request.data['payment_method'] else 'processing'
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

