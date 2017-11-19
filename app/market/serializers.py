from rest_framework import serializers

from app.market.models import Catalog, Category, Goods, Type, Size


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = [
            'id',
            'name',
            'price',
            'cover',
            'hover_cover',
        ]


class GoodsDetailSerializer(serializers.ModelSerializer):
    type = TypesSerializer()
    size = SizesSerializer(many=True, required=False)

    class Meta:
        model = Goods
        fields = [
            'id',
            'name',
            'type',
            'price',
            'description',
            'available',
            'cover',
            'hover_cover',
            'category',
            'is_active',
            'is_main',
            'width',
            'height',
            'length',
            'weight',
            'title',
            'audience',
            'accessibility',
            'easy_to_use',
            'author',
            'format',
            'count_pages',
            'date_publication',
            'size',
            'related_goods',
        ]


class CategorySerializer(serializers.ModelSerializer):
    goods_categories = GoodsSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'goods_categories', 'description']


class CatalogSerializer(serializers.ModelSerializer):
    catalogs = CategorySerializer(many=True)

    class Meta:
        model = Catalog
        fields = ['id', 'name', 'slug', 'catalogs']