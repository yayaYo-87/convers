from rest_framework import serializers

from app.market.models import Goods, Size
from app.market.serializers import CategorySerializer
from app.orders.models import OrderGoods, Cart, Order


class GoodsSerializer(serializers.ModelSerializer):
    type = CategorySerializer()
    class Meta:
        model = Goods
        fields = ['id', 'name', 'price', 'category',]


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']


class OrderGoodsSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(read_only=True)
    goods = GoodsSerializer()
    size = SizeSerializer()

    class Meta:
        model = OrderGoods
        fields = ['id', 'goods', 'size', 'count', 'price', 'created_at', 'active']

    def to_internal_value(self, data):
        self.fields['crocs'] = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all())
        self.fields['size'] = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all())
        return super(OrderGoodsSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        ordergoods = OrderGoods(**validated_data)

        request = self.context['request']
        value = request.session.session_key
        cart = Cart.objects.filter(cookie=value).first()
        ordergoods.cart = cart
        ordergoods.save()
        cart.save()

        return ordergoods


class CartSerializer(serializers.ModelSerializer):
    cart_goods = OrderGoodsSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = ['id', 'price', 'total_count', 'cart_goods', ]


class OrderSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(required=False)
    total = serializers.IntegerField(required=False)
    total_count = serializers.IntegerField(required=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'order_status',
            'total_count',
            'phone',
            'index',
            'first_name',
            'last_name',
            'address',
            'email',
            'city',
            'total',
            'created_at',
        ]


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'total_count',
            'order_status',
            'phone',
            'city',
            'address',
            'index',
            'name',
            'email',
            'phone',
            'total',
            'created_at',
            'goods',
        ]