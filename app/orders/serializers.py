from rest_framework import serializers

from app.market.models import Goods, Size
from app.market.serializers import TypesSerializer
from app.orders.models import OrderGoods, Cart, Order, Promocode


class GoodsSerializer(serializers.ModelSerializer):
    type = TypesSerializer()
    class Meta:
        model = Goods
        fields = ['id', 'name', 'price', 'category', 'type', 'cover', 'description']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']


class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = ['id', 'code', 'discount']


class OrderGoodsSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(read_only=True)
    goods = GoodsSerializer()
    size = SizeSerializer(required=False)

    class Meta:
        model = OrderGoods
        fields = ['id', 'goods', 'size', 'count', 'price', 'created_at', 'active', 'cart', 'order']

    def to_internal_value(self, data):
        self.fields['goods'] = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all())
        self.fields['size'] = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all(), required=False)
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
        fields = ['id', 'price', 'total_count', 'cart_goods', 'total_discount']


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
            'order_delivery',
            'home',
            'email',
            'city',
            'total',
            'total_delivery',
            'total_discount',
            'created_at',
            'shipping_id',
            'kladr_id',
            'delivery_point',
            'delivery_point_name',
            'administrative_area',
            'settlement',
            'apartment',
            'comment',
        ]


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'total_count',
            'order_status',
            'order_delivery',
            'phone',
            'city',
            'address',
            'home',
            'index',
            'first_name',
            'last_name',
            'email',
            'phone',
            'total',
            'total_delivery',
            'total_discount',
            'created_at',
            'goods',
        ]